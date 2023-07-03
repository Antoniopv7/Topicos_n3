CREATE OR REPLACE PROCEDURE insertar_cliente(
  p_nombre VARCHAR(30),
  p_apellido VARCHAR(30),
  p_rut VARCHAR(30),
  p_direccion VARCHAR(30),
  p_telefono INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
  -- Verificar si el cliente ya existe por su rut
  IF p_rut IS NULL THEN
    RAISE EXCEPTION 'El campo "rut" no puede ser nulo';
  END IF;
  
  IF EXISTS (SELECT 1 FROM cliente WHERE rut = p_rut) THEN
    RAISE EXCEPTION 'El cliente con rut % ya existe', p_rut;
  END IF;
  
  -- Insertar el nuevo cliente
  BEGIN
    INSERT INTO cliente (nombre, apellido, rut, direccion, telefono)
    VALUES (p_nombre, p_apellido, p_rut, p_direccion, p_telefono);
    
    EXCEPTION
      WHEN OTHERS THEN
        RAISE EXCEPTION 'Error al insertar el cliente: %', SQLERRM;
  END;
  
EXCEPTION
  WHEN OTHERS THEN
    -- Manejar errores generales
    RAISE EXCEPTION 'Error al insertar el cliente: %', SQLERRM;
END;
$$;
----------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_empleado(
    p_nombre VARCHAR(30),
    p_apellido VARCHAR(30),
    p_rut VARCHAR(30),
    p_sueldo INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el empleado ya existe por su rut
    IF p_rut IS NULL THEN
        RAISE EXCEPTION 'El campo "rut" no puede ser nulo';
    END IF;
  
    IF EXISTS (SELECT 1 FROM empleado WHERE rut = p_rut) THEN
        RAISE EXCEPTION 'El empleado con rut % ya existe', p_rut;
    END IF;
  
    -- Insertar el nuevo empleado
    BEGIN
        INSERT INTO empleado (nombre, apellido, rut, sueldo)
        VALUES (p_nombre, p_apellido, p_rut, p_sueldo);
    
    EXCEPTION
        WHEN OTHERS THEN
            RAISE EXCEPTION 'Error al insertar el empleado: %', SQLERRM;
    END;
  
EXCEPTION
    WHEN OTHERS THEN
        -- Manejar errores generales
        RAISE EXCEPTION 'Error al insertar el empleado: %', SQLERRM;
END;
$$;
-----------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_producto(
    p_nombre VARCHAR(30),
    p_descripcion VARCHAR(30),
    p_valor INTEGER,
    p_stock INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el producto ya existe por su nombre
    IF p_nombre IS NULL THEN
        RAISE EXCEPTION 'El campo "nombre" no puede ser nulo';
    END IF;
  
    IF EXISTS (SELECT 1 FROM producto WHERE nombre = p_nombre) THEN
        RAISE EXCEPTION 'El producto con nombre % ya existe', p_nombre;
    END IF;
  
    -- Insertar el nuevo producto
    BEGIN
        INSERT INTO producto (nombre, descripcion, valor, stock)
        VALUES (p_nombre, p_descripcion, p_valor, p_stock);
    
    EXCEPTION
        WHEN OTHERS THEN
            RAISE EXCEPTION 'Error al insertar el producto: %', SQLERRM;
    END;
  
EXCEPTION
    WHEN OTHERS THEN
        -- Manejar errores generales
        RAISE EXCEPTION 'Error al insertar el producto: %', SQLERRM;
END;
$$;
-------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_proveedor(
    p_producto_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el proveedor ya existe por su ID de producto
    IF p_producto_id IS NULL THEN
        RAISE EXCEPTION 'El campo "producto_id" no puede ser nulo';
    END IF;
  
    IF EXISTS (SELECT 1 FROM proveedor WHERE producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'El proveedor con ID de producto % ya existe', p_producto_id;
    END IF;
	
	IF NOT EXISTS (SELECT 1 FROM producto WHERE producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'El producto con id % no existe', p_producto_id;
    END IF;
  
    -- Insertar el nuevo proveedor
    BEGIN
        INSERT INTO proveedor (producto_id)
        VALUES (p_producto_id);
    
    EXCEPTION
        WHEN OTHERS THEN
            RAISE EXCEPTION 'Error al insertar el proveedor: %', SQLERRM;
    END;
  
EXCEPTION
    WHEN OTHERS THEN
        -- Manejar errores generales
        RAISE EXCEPTION 'Error al insertar el proveedor: %', SQLERRM;
END;
$$;
--------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_pedido(p_fecha DATE, p_monto_total INTEGER, p_cliente_id INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el cliente existe
    IF NOT EXISTS (SELECT 1 FROM cliente WHERE cliente_id = p_cliente_id) THEN
        RAISE EXCEPTION 'El cliente con id % no existe', p_cliente_id;
    END IF;
  
    -- Insertar el nuevo pedido
    BEGIN
        INSERT INTO pedido (fecha, monto_total, cliente_id)
        VALUES (p_fecha, p_monto_total, p_cliente_id);
    
    EXCEPTION
        WHEN OTHERS THEN
            RAISE EXCEPTION 'Error al insertar el pedido: %', SQLERRM;
    END;
  
EXCEPTION
    WHEN OTHERS THEN
        -- Manejar errores generales
        RAISE EXCEPTION 'Error al insertar el pedido: %', SQLERRM;
END;
$$;
--------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_boleta(
    p_cliente_id INTEGER,
    p_detalle_venta VARCHAR(30),
    p_monto_neto INTEGER,
    p_monto_iva INTEGER,
    p_monto_total INTEGER,
    p_fecha DATE,
    p_cod_pago INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el cliente existe
    IF NOT EXISTS (SELECT 1 FROM cliente WHERE cliente_id = p_cliente_id) THEN
        RAISE EXCEPTION 'El cliente con id % no existe', p_cliente_id;
    END IF;
	
	-- Verificar si el cod_pago
	IF NOT EXISTS (SELECT 1 FROM pedido WHERE cod_pago = p_cod_pago) THEN
        RAISE EXCEPTION 'El pago con código % no existe', p_cod_pago;
    END IF;
  
    -- Insertar la nueva boleta
    BEGIN
        INSERT INTO boleta (cliente_id, detalle_venta, monto_neto, monto_iva, monto_total, fecha, cod_pago)
        VALUES (p_cliente_id, p_detalle_venta, p_monto_neto, p_monto_iva, p_monto_total, p_fecha, p_cod_pago);
    
    EXCEPTION
        WHEN OTHERS THEN
            RAISE EXCEPTION 'Error al insertar la boleta: %', SQLERRM;
    END;
  
EXCEPTION
    WHEN OTHERS THEN
        -- Manejar errores generales
        RAISE EXCEPTION 'Error al insertar la boleta: %', SQLERRM;
END;
$$;
-------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_despacho(
    p_fecha DATE,
    p_hora_salida TIME,
    p_hora_entrega TIME,
    p_cliente_id INTEGER,
    p_empleado_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el cliente existe
    IF NOT EXISTS (SELECT 1 FROM cliente WHERE cliente_id = p_cliente_id) THEN
        RAISE EXCEPTION 'El cliente con id % no existe', p_cliente_id;
    END IF;

    -- Verificar si el empleado existe
    IF NOT EXISTS (SELECT 1 FROM empleado WHERE empleado_id = p_empleado_id) THEN
        RAISE EXCEPTION 'El empleado con id % no existe', p_empleado_id;
    END IF;

    -- Insertar en la tabla DESPACHO
    INSERT INTO despacho (fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
    VALUES (p_fecha, p_hora_salida, p_hora_entrega, p_cliente_id, p_empleado_id);
    
    -- Mostrar mensaje de éxito
    RAISE NOTICE 'Despacho insertado correctamente.';
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al insertar en la tabla DESPACHO: %', SQLERRM;
END;
$$;
------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_pago(
    p_estado BOOLEAN,
    p_monto_total INTEGER,
    p_cod_pago INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el código de pago existe
    IF NOT EXISTS (SELECT 1 FROM pedido WHERE cod_pago = p_cod_pago) THEN
        RAISE EXCEPTION 'El pago con código % no existe', p_cod_pago;
    END IF;
  
    -- Insertar en la tabla PAGO
    INSERT INTO pago (estado, monto_total, cod_pago)
    VALUES (p_estado, p_monto_total, p_cod_pago);
    
    -- Mostrar mensaje de éxito
    RAISE NOTICE 'Pago insertado correctamente.';
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al insertar en la tabla PAGO: %', SQLERRM;
END;
$$;
----------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE insertar_factura(
    p_proveedor_id INTEGER,
    p_producto_id INTEGER,
    p_tipo_producto VARCHAR(30),
    p_monto_total INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el proveedor existe
    IF NOT EXISTS (SELECT 1 FROM proveedor WHERE proveedor_id = p_proveedor_id) THEN
        RAISE EXCEPTION 'El proveedor con id % no existe', p_proveedor_id;
    END IF;

    -- Verificar si el producto existe
    IF NOT EXISTS (SELECT 1 FROM producto WHERE producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'El producto con id % no existe', p_producto_id;
    END IF;

    -- Insertar en la tabla FACTURA
    INSERT INTO factura (proveedor_id, producto_id, tipo_producto, monto_total)
    VALUES (p_proveedor_id, p_producto_id, p_tipo_producto, p_monto_total);
    
    -- Mostrar mensaje de éxito
    RAISE NOTICE 'Factura insertada correctamente.';
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al insertar en la tabla FACTURA: %', SQLERRM;
END;
$$;
----------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE eliminar_cliente(id_cliente INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    IF id_cliente IS NULL THEN
        RAISE EXCEPTION 'Debe proporcionar un id de cliente.';
    END IF;
    
    DELETE FROM CLIENTE WHERE cliente_id = id_cliente;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Cliente con id % no encontrado.', id_cliente;
    END IF;
    
    RAISE NOTICE 'Cliente con id % ha sido eliminado.', id_cliente;
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al insertar en la tabla FACTURA: %', SQLERRM;
END;
$$;
----------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE eliminar_empleado(id_empleado INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    IF id_empleado IS NULL THEN
        RAISE EXCEPTION 'Debe proporcionar un id de empleado.';
    END IF;
    
    DELETE FROM EMPLEADO WHERE empleado_id = id_empleado;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Empleado con id % no encontrado.', id_empleado;
    END IF;
    
    RAISE NOTICE 'Empleado con id % ha sido eliminado.', id_empleado;
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al eliminar de la tabla EMPLEADO: %', SQLERRM;
END;
$$;
--------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE eliminar_despacho(id_despacho INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    IF id_despacho IS NULL THEN
        RAISE EXCEPTION 'Debe proporcionar un ID de despacho.';
    END IF;
    
    DELETE FROM DESPACHO WHERE despacho_id = id_despacho;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Despacho con ID % no encontrado.', id_despacho;
    END IF;
    
    RAISE NOTICE 'Despacho con ID % ha sido eliminado.', id_despacho;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error al eliminar de la tabla DESPACHO: %', SQLERRM;
END;
$$;
--------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE eliminar_pago(id_pago INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    IF id_pago IS NULL THEN
        RAISE EXCEPTION 'Debe proporcionar un codigo de pago.';
    END IF;
    
    DELETE FROM pago WHERE cod_pago = id_pago;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Pago con codigo % no encontrado.', id_pago;
    END IF;
    
    RAISE NOTICE 'Pago con codigo % ha sido eliminado.', id_pago;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error al eliminar de la tabla PAGO: %', SQLERRM;
END;
$$;
---------------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE eliminar_producto(id_producto INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    IF id_producto IS NULL THEN
        RAISE EXCEPTION 'Debe proporcionar un codigo de producto.';
    END IF;
    
    DELETE FROM producto WHERE producto_id = id_producto;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Producto con codigo % no encontrado.', id_producto;
    END IF;
    
    RAISE NOTICE 'Producto con codigo % ha sido eliminado.', id_producto;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error al eliminar de la tabla PRODUCTO: %', SQLERRM;
END;
$$;
------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE eliminar_proveedor(id_proveedor INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    IF id_proveedor IS NULL THEN
        RAISE EXCEPTION 'Debe proporcionar un codigo de proveedor.';
    END IF;
    
    DELETE FROM proveedor WHERE proveedor_id = id_proveedor;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Proveedor con codigo % no encontrado.', id_proveedor;
    END IF;
    
    RAISE NOTICE 'Proveedor con codigo % ha sido eliminado.', id_proveedor;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error al eliminar de la tabla PROVEEDOR: %', SQLERRM;
END;
$$;
---------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE PROCEDURE eliminar_pedido(codigo_ped INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    IF codigo_ped IS NULL THEN
        RAISE EXCEPTION 'Debe proporcionar un codigo de pedido.';
    END IF;
    
    DELETE FROM pedido WHERE cod_pago = codigo_ped;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Pedido con codigo % no encontrado.', codigo_ped;
    END IF;
    
    RAISE NOTICE 'Pedido con codigo % ha sido eliminado.', codigo_ped;
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error al eliminar de la tabla PEDIDO: %', SQLERRM;
END;
$$;