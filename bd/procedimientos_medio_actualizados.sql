CREATE OR REPLACE PROCEDURE insertar_cliente(
  p_cliente_id INTEGER,
  p_nombre VARCHAR(30),
  p_apellido VARCHAR(30),
  p_rut VARCHAR(30),
  p_direccion VARCHAR(30),
  p_telefono INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
  -- Validar que el cliente con ID no exista
  IF EXISTS (SELECT 1 FROM cliente WHERE cliente_id = p_cliente_id) THEN
    RAISE EXCEPTION 'El cliente con ID % ya existe', p_cliente_id;
  END IF;

  -- Validar que el campo cliente_id no sea nulo
  IF p_cliente_id IS NULL THEN
    RAISE EXCEPTION 'El campo "cliente_id" no puede ser nulo';
  END IF;
  
  -- Validar que el campo rut no sea nulo
  IF p_rut IS NULL THEN
    RAISE EXCEPTION 'El campo "rut" no puede ser nulo';
  END IF;
  
  -- Validar que el cliente con rut no exista
  IF EXISTS (SELECT 1 FROM cliente WHERE rut = p_rut) THEN
    RAISE EXCEPTION 'El cliente con rut % ya existe', p_rut;
  END IF;
  
  -- Insertar el nuevo cliente
  BEGIN
    INSERT INTO cliente (cliente_id, nombre, apellido, rut, direccion, telefono)
    VALUES (p_cliente_id, p_nombre, p_apellido, p_rut, p_direccion, p_telefono);
    
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

CREATE OR REPLACE PROCEDURE insertar_empleado(
    p_empleado_id INTEGER,
    p_nombre VARCHAR(30),
    p_apellido VARCHAR(30),
    p_rut VARCHAR(30),
    p_sueldo INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el campo empleado_id no es nulo
    IF p_empleado_id IS NULL THEN
        RAISE EXCEPTION 'El campo "empleado_id" no puede ser nulo';
    END IF;
  
    -- Verificar si el campo rut no es nulo
    IF p_rut IS NULL THEN
        RAISE EXCEPTION 'El campo "rut" no puede ser nulo';
    END IF;
  
    -- Verificar si el empleado con empleado_id ya existe
    IF EXISTS (SELECT 1 FROM empleado WHERE empleado_id = p_empleado_id) THEN
        RAISE EXCEPTION 'El empleado con ID % ya existe', p_empleado_id;
    END IF;
  
    -- Verificar si el empleado con rut ya existe
    IF EXISTS (SELECT 1 FROM empleado WHERE rut = p_rut) THEN
        RAISE EXCEPTION 'El empleado con rut % ya existe', p_rut;
    END IF;
  
    -- Insertar el nuevo empleado
    BEGIN
        INSERT INTO empleado (empleado_id, nombre, apellido, rut, sueldo)
        VALUES (p_empleado_id, p_nombre, p_apellido, p_rut, p_sueldo);
    
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

CREATE OR REPLACE PROCEDURE insertar_producto(
    p_producto_id INTEGER,
    p_nombre VARCHAR(30),
    p_descripcion VARCHAR(30),
    p_valor INTEGER,
    p_stock INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el campo producto_id no es nulo
    IF p_producto_id IS NULL THEN
        RAISE EXCEPTION 'El campo "producto_id" no puede ser nulo';
    END IF;

    -- Verificar si el campo nombre no es nulo
    IF p_nombre IS NULL THEN
        RAISE EXCEPTION 'El campo "nombre" no puede ser nulo';
    END IF;

    -- Verificar si el producto con producto_id ya existe
    IF EXISTS (SELECT 1 FROM producto WHERE producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'El producto con ID % ya existe', p_producto_id;
    END IF;

    -- Verificar si el producto con nombre ya existe
    IF EXISTS (SELECT 1 FROM producto WHERE nombre = p_nombre) THEN
        RAISE EXCEPTION 'El producto con nombre % ya existe', p_nombre;
    END IF;

    -- Insertar el nuevo producto
    BEGIN
        INSERT INTO producto (producto_id, nombre, descripcion, valor, stock)
        VALUES (p_producto_id, p_nombre, p_descripcion, p_valor, p_stock);

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

CREATE OR REPLACE PROCEDURE insertar_proveedor(
    p_proveedor_id INTEGER,
    p_producto_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el campo proveedor_id no es nulo
    IF p_proveedor_id IS NULL THEN
        RAISE EXCEPTION 'El campo "proveedor_id" no puede ser nulo';
    END IF;

    -- Verificar si el campo producto_id no es nulo
    IF p_producto_id IS NULL THEN
        RAISE EXCEPTION 'El campo "producto_id" no puede ser nulo';
    END IF;

    -- Verificar si el proveedor con proveedor_id ya existe
    IF EXISTS (SELECT 1 FROM proveedor WHERE proveedor_id = p_proveedor_id) THEN
        RAISE EXCEPTION 'El proveedor con ID % ya existe', p_proveedor_id;
    END IF;

    -- Verificar si el proveedor con producto_id ya existe
    IF EXISTS (SELECT 1 FROM proveedor WHERE producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'El proveedor con ID de producto % ya existe', p_producto_id;
    END IF;

    -- Verificar si el producto con producto_id existe
    IF NOT EXISTS (SELECT 1 FROM producto WHERE producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'El producto con ID % no existe', p_producto_id;
    END IF;

    -- Insertar el nuevo proveedor
    BEGIN
        INSERT INTO proveedor (proveedor_id, producto_id)
        VALUES (p_proveedor_id, p_producto_id);

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

CREATE OR REPLACE PROCEDURE insertar_pedido(p_cod_pago INTEGER, p_fecha DATE, p_producto_id INTEGER, p_cliente_id INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el campo cod_pago no es nulo
    IF p_cod_pago IS NULL THEN
        RAISE EXCEPTION 'El campo "cod_pago" no puede ser nulo';
    END IF;

    -- Verificar si el cliente con cliente_id existe
    IF NOT EXISTS (SELECT 1 FROM cliente WHERE cliente_id = p_cliente_id) THEN
        RAISE EXCEPTION 'El cliente con ID % no existe', p_cliente_id;
    END IF;

    -- Verificar si el producto con producto_id existe
    IF NOT EXISTS (SELECT 1 FROM producto WHERE producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'El producto con ID % no existe', p_producto_id;
    END IF;

    -- Verificar si el pedido con cod_pago ya existe
    IF EXISTS (SELECT 1 FROM pedido WHERE cod_pago = p_cod_pago) THEN
        RAISE EXCEPTION 'El pedido con cod_pago % ya existe', p_cod_pago;
    END IF;

    -- Insertar el nuevo pedido
    BEGIN
        INSERT INTO pedido (cod_pago, fecha, producto_id, cliente_id)
        VALUES (p_cod_pago, p_fecha, p_producto_id, p_cliente_id);

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

CREATE OR REPLACE PROCEDURE insertar_despacho(
    p_despacho_id INTEGER,
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
        RAISE EXCEPTION 'El cliente con ID % no existe', p_cliente_id;
    END IF;

    -- Verificar si el empleado existe
    IF NOT EXISTS (SELECT 1 FROM empleado WHERE empleado_id = p_empleado_id) THEN
        RAISE EXCEPTION 'El empleado con ID % no existe', p_empleado_id;
    END IF;

    -- Verificar si el despacho con despacho_id ya existe
    IF EXISTS (SELECT 1 FROM despacho WHERE despacho_id = p_despacho_id) THEN
        RAISE EXCEPTION 'El despacho con ID % ya existe', p_despacho_id;
    END IF;

    -- Insertar en la tabla DESPACHO
    INSERT INTO despacho (despacho_id, fecha, hora_salida, hora_entrega, cliente_id, empleado_id)
    VALUES (p_despacho_id, p_fecha, p_hora_salida, p_hora_entrega, p_cliente_id, p_empleado_id);

    -- Mostrar mensaje de éxito
    RAISE NOTICE 'Despacho insertado correctamente.';
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al insertar en la tabla DESPACHO: %', SQLERRM;
END;
$$;

CREATE OR REPLACE PROCEDURE insertar_pago(
    p_estado BOOLEAN,
    p_cod_pago INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el código de pago existe
    IF NOT EXISTS (SELECT 1 FROM pedido WHERE cod_pago = p_cod_pago) THEN
        RAISE EXCEPTION 'El pago con código % no existe', p_cod_pago;
    END IF;
	
	-- Verificar si el código de pago existe
    IF EXISTS (SELECT 1 FROM pago WHERE cod_pago = p_cod_pago) THEN
        RAISE EXCEPTION 'El pago con código % ya existe', p_cod_pago;
    END IF;
  
    -- Insertar en la tabla PAGO
    INSERT INTO pago (estado, cod_pago)
    VALUES (p_estado, p_cod_pago);
    
    -- Mostrar mensaje de éxito
    RAISE NOTICE 'Pago insertado correctamente.';
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al insertar en la tabla PAGO: %', SQLERRM;
END;
$$;

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
    
    -- Verificar si ya existe una factura con el mismo ID
    IF EXISTS (SELECT 1 FROM factura WHERE proveedor_id = p_proveedor_id AND producto_id = p_producto_id) THEN
        RAISE EXCEPTION 'Ya existe una factura para el proveedor con id % y el producto con id %', p_proveedor_id, p_producto_id;
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

CREATE OR REPLACE PROCEDURE modificar_pago(
    p_cod_pago INTEGER,
    p_estado BOOLEAN
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificar si el pago existe
    IF NOT EXISTS (SELECT 1 FROM pago WHERE cod_pago = p_cod_pago) THEN
        RAISE EXCEPTION 'El pago con código % no existe', p_cod_pago;
    END IF;

    -- Modificar el estado del pago
    UPDATE pago
    SET estado = p_estado
    WHERE cod_pago = p_cod_pago;
    
    -- Mostrar mensaje de éxito
    RAISE NOTICE 'Pago modificado correctamente.';
EXCEPTION
    WHEN OTHERS THEN
        -- Mostrar mensaje de error
        RAISE EXCEPTION 'Error al modificar el pago: %', SQLERRM;
END;
$$;

CREATE OR REPLACE PROCEDURE modificar_despacho(
    p_despacho_id INTEGER,
    p_fecha DATE,
    p_hora_salida TIME,
    p_hora_entrega TIME,
    p_cliente_id INTEGER,
    p_empleado_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Verificamos que el ID no sea nulo
    IF p_despacho_id IS NULL THEN
        RAISE EXCEPTION 'El despacho_id no puede ser nulo';
    END IF;

    UPDATE DESPACHO
    SET 
        fecha = p_fecha,
        hora_salida = p_hora_salida,
        hora_entrega = p_hora_entrega,
        cliente_id = p_cliente_id,
        empleado_id = p_empleado_id
    WHERE 
        despacho_id = p_despacho_id;

    IF NOT FOUND THEN
        RAISE WARNING 'Despacho con ID % no encontrado', p_despacho_id;
    END IF;

EXCEPTION
    WHEN unique_violation THEN
        RAISE EXCEPTION 'El despacho_id % ya existe', p_despacho_id;
    WHEN others THEN
        RAISE EXCEPTION 'Ha ocurrido un error inesperado: %', SQLERRM;
END;
$$;

CREATE OR REPLACE PROCEDURE modificar_cliente(
    _cliente_id INTEGER,
    _nombre VARCHAR(30),
    _apellido VARCHAR(30),
    _rut VARCHAR(30),
    _direccion VARCHAR(30),
    _telefono INTEGER
)
LANGUAGE plpgsql
AS
$$
BEGIN
	
	IF EXISTS (SELECT 1 FROM cliente WHERE rut = _rut) THEN
        RAISE EXCEPTION 'El cliente con rut % ya existe', _rut;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM cliente WHERE cliente_id = _cliente_id) THEN
        RAISE 'Cliente con id % no encontrado', _cliente_id;
    ELSIF _nombre IS NULL OR _apellido IS NULL OR _rut IS NULL OR _direccion IS NULL THEN
        RAISE 'El rut debe tener exactamente 30 caracteres';
    ELSIF LENGTH(_nombre) > 30 OR LENGTH(_apellido) > 30 OR LENGTH(_direccion) > 30 THEN
        RAISE 'Los campos nombre, apellido y dirección no pueden tener más de 30 caracteres';
    ELSIF _telefono < 0 THEN
        RAISE 'El teléfono no puede ser un número negativo';
    ELSE
        UPDATE cliente
        SET nombre = _nombre,
            apellido = _apellido,
            rut = _rut,
            direccion = _direccion,
            telefono = _telefono
        WHERE cliente_id = _cliente_id;
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE 'Error inesperado: %', SQLERRM;
END;
$$;

CREATE OR REPLACE PROCEDURE modificar_empleado(
    _empleado_id INTEGER,
    _nombre VARCHAR(30),
    _apellido VARCHAR(30),
    _rut VARCHAR(30),
    _sueldo INTEGER
)
LANGUAGE plpgsql
AS
$$
BEGIN

	IF EXISTS (SELECT 1 FROM empleado WHERE rut = _rut) THEN
        RAISE EXCEPTION 'El empleado con rut % ya existe', _rut;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM EMPLEADO WHERE empleado_id = _empleado_id) THEN
        RAISE 'Empleado con id % no encontrado', _empleado_id;
    ELSIF _nombre IS NULL OR _apellido IS NULL OR _rut IS NULL THEN
        RAISE 'Los campos nombre, apellido y rut no pueden ser nulos';
    ELSIF LENGTH(_nombre) > 30 OR LENGTH(_apellido) > 30 THEN
        RAISE 'Los campos nombre y apellido no pueden tener más de 30 caracteres';
    ELSIF _sueldo < 0 THEN
        RAISE 'El sueldo no puede ser un número negativo';
    ELSE
        UPDATE EMPLEADO
        SET nombre = _nombre,
            apellido = _apellido,
            rut = _rut,
            sueldo = _sueldo
        WHERE empleado_id = _empleado_id;
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE 'Error inesperado: %', SQLERRM;
END;
$$;

CREATE OR REPLACE PROCEDURE modificar_pedido(
    _cod_pago INTEGER,
    _fecha DATE,
    _producto_id INTEGER,
    _cliente_id INTEGER
)
LANGUAGE plpgsql
AS
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM PEDIDO WHERE cod_pago = _cod_pago) THEN
        RAISE 'Pedido con código de pago % no encontrado', _cod_pago;
    ELSIF _fecha IS NULL OR _producto_id IS NULL OR _cliente_id IS NULL THEN
        RAISE 'Los campos fecha, producto_id y cliente_id no pueden ser nulos';
    ELSE
        UPDATE PEDIDO
        SET fecha = _fecha,
            producto_id = _producto_id,
            cliente_id = _cliente_id
        WHERE cod_pago = _cod_pago;
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE 'Error inesperado: %', SQLERRM;
END;
$$;

CREATE OR REPLACE PROCEDURE modificar_proveedor(
    _proveedor_id INTEGER,
    _producto_id INTEGER
)
LANGUAGE plpgsql
AS
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM PROVEEDOR WHERE proveedor_id = _proveedor_id) THEN
        RAISE 'Proveedor con id % no encontrado', _proveedor_id;
    ELSIF _producto_id IS NULL THEN
        RAISE 'El campo producto_id no puede ser nulo';
    ELSE
        UPDATE PROVEEDOR
        SET producto_id = _producto_id
        WHERE proveedor_id = _proveedor_id;
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE 'Error inesperado: %', SQLERRM;
END;
$$;

CREATE OR REPLACE PROCEDURE modificar_producto(
    _producto_id INTEGER,
    _nombre VARCHAR(30),
    _descripcion VARCHAR(30),
    _valor INTEGER,
    _stock INTEGER
)
LANGUAGE plpgsql
AS
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM PRODUCTO WHERE producto_id = _producto_id) THEN
        RAISE 'Producto con id % no encontrado', _producto_id;
    ELSIF _nombre IS NULL OR _descripcion IS NULL THEN
        RAISE 'Los campos nombre y descripción no pueden ser nulos';
    ELSIF LENGTH(_nombre) > 30 OR LENGTH(_descripcion) > 30 THEN
        RAISE 'Los campos nombre y descripción no pueden tener más de 30 caracteres';
    ELSIF _valor < 0 THEN
        RAISE 'El valor no puede ser un número negativo';
    ELSIF _stock < 0 THEN
        RAISE 'El stock no puede ser un número negativo';
    ELSE
        UPDATE PRODUCTO
        SET nombre = _nombre,
            descripcion = _descripcion,
            valor = _valor,
            stock = _stock
        WHERE producto_id = _producto_id;
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE 'Error inesperado: %', SQLERRM;
END;
$$;
