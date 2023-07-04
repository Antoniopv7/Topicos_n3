CREATE OR REPLACE FUNCTION check_producto_monto() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.valor > 1000000 THEN
        RAISE EXCEPTION 'El valor del producto no puede exceder el 1,000,000';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_producto_monto_trigger
BEFORE INSERT OR UPDATE ON producto
FOR EACH ROW
EXECUTE FUNCTION check_producto_monto();

CREATE OR REPLACE FUNCTION generate_boleta()
  RETURNS TRIGGER AS
$$
BEGIN
  DECLARE
    id_cliente INTEGER;
    total_monto INTEGER;
  BEGIN
    SELECT
      pe.cliente_id,
      pr.valor
    INTO
      id_cliente,
      total_monto
    FROM
      PEDIDO pe
    JOIN
      PRODUCTO pr ON pe.producto_id = pr.producto_id
    WHERE
      pe.cod_pago = NEW.cod_pago;

    IF NEW.estado = TRUE THEN
      INSERT INTO BOLETA (cliente_id, detalle_venta, monto_neto, monto_iva, monto_total, fecha, cod_pago)
      VALUES (id_cliente, 'Venta', total_monto * 0.8, total_monto * 0.2, total_monto, CURRENT_DATE, NEW.cod_pago);
    END IF;

    RETURN NEW;
  END;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER generate_boleta_trigger
AFTER INSERT OR UPDATE ON PAGO
FOR EACH ROW
WHEN (NEW.estado = TRUE)
EXECUTE FUNCTION generate_boleta();



DROP TRIGGER generate_boleta_trigger on pago; 
DROP TRIGGER generate_despacho_trigger on pago;

CREATE OR REPLACE FUNCTION generar_despacho()
  RETURNS TRIGGER AS
$$
DECLARE
  id_cliente INTEGER;
  nuevo_despacho_id INTEGER;
BEGIN
  SELECT cliente_id INTO id_cliente FROM PEDIDO WHERE cod_pago = NEW.cod_pago;

  -- Generar un número aleatorio para despacho_id
  LOOP
    -- Generar un número aleatorio entre 1 y 100000 (puedes ajustar este rango según tus necesidades)
    nuevo_despacho_id := (RANDOM() * 100)::INTEGER;

    -- Verificar si este id ya existe en la tabla DESPACHO
    EXIT WHEN NOT EXISTS (SELECT 1 FROM DESPACHO WHERE despacho_id = nuevo_despacho_id);
  END LOOP;

  -- Añadir una declaración de depuración
  RAISE NOTICE 'nuevo_despacho_id es %', nuevo_despacho_id;

  IF NEW.estado = TRUE AND nuevo_despacho_id IS NOT NULL THEN
    INSERT INTO DESPACHO (despacho_id, fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
    SELECT nuevo_despacho_id, CURRENT_DATE, CURRENT_TIME, CURRENT_TIME + INTERVAL '1 hour', id_cliente, empleado_id
    FROM EMPLEADO
    ORDER BY RANDOM()
    LIMIT 1;
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER generate_despacho_trigger
AFTER INSERT OR UPDATE ON PAGO
FOR EACH ROW
WHEN (NEW.estado = TRUE)
EXECUTE FUNCTION generate_despacho();

CREATE OR REPLACE FUNCTION generar_factura()
  RETURNS TRIGGER AS
$$
DECLARE
  total_monto INTEGER;
BEGIN
  SELECT valor*stock INTO total_monto FROM PRODUCTO WHERE producto_id = NEW.producto_id;

  INSERT INTO FACTURA (proveedor_id, producto_id, tipo_producto, monto_total)
  VALUES (NEW.proveedor_id, NEW.producto_id, (SELECT Descripcion FROM PRODUCTO WHERE producto_id = NEW.producto_id), total_monto);

  RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER generar_factura_trigger
AFTER INSERT ON PROVEEDOR
FOR EACH ROW
EXECUTE FUNCTION generar_factura();

CREATE OR REPLACE FUNCTION respaldar_despacho()
  RETURNS TRIGGER AS
$$
BEGIN
  INSERT INTO respaldo_despacho (despacho_id, fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
  SELECT despacho.despacho_id, despacho.fecha, despacho.hora_salida, despacho.hora_entrega, despacho.cliente_id, despacho.empleado_id
  FROM despacho
  WHERE despacho.despacho_id = OLD.despacho_id;
  
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER respaldo_despacho_trigger
BEFORE DELETE ON pedido
FOR EACH ROW
WHEN (NEW.estado = TRUE)
EXECUTE FUNCTION respaldar_despacho();

CREATE OR REPLACE FUNCTION respaldar_factura()
  RETURNS TRIGGER AS
$$
BEGIN
  INSERT INTO respaldo_factura (proveedor_id, producto_id, tipo_producto, monto_total)
  SELECT factura.proveedor_id, factura.producto_id, factura.tipo_producto, factura.monto_total
  FROM factura
  WHERE factura.producto_id = OLD.producto_id;
  
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER respaldo_factura_trigger
BEFORE DELETE ON producto
FOR EACH ROW
EXECUTE FUNCTION respaldar_factura();

CREATE OR REPLACE FUNCTION respaldar_boleta()
  RETURNS TRIGGER AS
$$
BEGIN
  INSERT INTO respaldo_boleta (cliente_id, detalle_venta, monto_neto, monto_iva, monto_total, fecha, cod_pago)
  SELECT boleta.cliente_id, boleta.detalle_venta, boleta.monto_neto, boleta.monto_iva, boleta.monto_total, boleta.fecha, boleta.cod_pago
  FROM boleta
  WHERE boleta.cod_pago = OLD.cod_pago;
  
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER respaldo_boleta_trigger
BEFORE DELETE ON pedido
FOR EACH ROW
EXECUTE FUNCTION respaldar_boleta();
