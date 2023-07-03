CREATE OR REPLACE FUNCTION check_pago_monto() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.monto_total > 1000000 THEN
        RAISE EXCEPTION 'El monto total no puede exceder 1,000,000';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_pago_monto_trigger
BEFORE INSERT OR UPDATE ON PAGO
FOR EACH ROW
EXECUTE FUNCTION check_pago_monto();
----------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION generate_boleta() RETURNS TRIGGER AS $$
DECLARE
    id_cliente INTEGER;
    total_monto INTEGER;
BEGIN
    SELECT cliente_id, monto_total INTO id_cliente, total_monto FROM PEDIDO WHERE cod_pago = NEW.cod_pago;

    IF NEW.estado = TRUE THEN
        INSERT INTO BOLETA (cliente_id, detalle_venta, monto_neto, monto_iva, monto_total, fecha, cod_pago)
        VALUES (id_cliente, 'Venta', total_monto * 0.8, total_monto * 0.2, total_monto, CURRENT_DATE, NEW.cod_pago);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER generate_boleta_trigger
AFTER INSERT OR UPDATE ON PAGO
FOR EACH ROW
WHEN (NEW.estado = TRUE)
EXECUTE FUNCTION generate_boleta();


DROP TRIGGER generate_boleta_trigger on pago; 
DROP TRIGGER generate_despacho_trigger on pago;
-------------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION generate_despacho() RETURNS TRIGGER AS $$
DECLARE
    id_cliente INTEGER;
BEGIN
    SELECT cliente_id INTO id_cliente FROM PEDIDO WHERE cod_pago = NEW.cod_pago;

    IF NEW.estado = TRUE THEN
        INSERT INTO DESPACHO (fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
        VALUES (CURRENT_DATE, CURRENT_TIME, CURRENT_TIME + INTERVAL '1 hour', id_cliente, 1);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER generate_despacho_trigger
AFTER INSERT OR UPDATE ON PAGO
FOR EACH ROW
WHEN (NEW.estado = TRUE)
EXECUTE FUNCTION generate_despacho();