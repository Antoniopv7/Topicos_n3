CREATE TABLE CLIENTE
(
    cliente_id INTEGER PRIMARY KEY,
    nombre     VARCHAR (30),
    apellido   VARCHAR (30),
    rut        VARCHAR (30),
    direccion  VARCHAR (30),
    telefono   INTEGER
);

CREATE TABLE DESPACHO
(
    despacho_id   INTEGER PRIMARY KEY ,
    fecha         DATE,
    hora_salida   TIME,
    hora_entrega  TIME,
    cliente_id    INTEGER,
    empleado_id   INTEGER 
);

CREATE TABLE PRODUCTO
( 
    producto_id INTEGER PRIMARY KEY,
	nombre      VARCHAR(30) ,
    descripcion VARCHAR(30),
    valor       INTEGER  ,
    stock       INTEGER 
);

CREATE TABLE PEDIDO
(
    cod_pago       INTEGER PRIMARY KEY,
    fecha          DATE,
	producto_id    INTEGER,
    cliente_id     INTEGER 
);

CREATE TABLE FACTURA
(
    proveedor_id    INTEGER,
    producto_id     INTEGER,
    tipo_producto   VARCHAR(30),
    monto_total     INTEGER 
);

CREATE TABLE PROVEEDOR 
(
    proveedor_id    INTEGER PRIMARY KEY,
    producto_id     INTEGER 
);

CREATE TABLE BOLETA
(
    cliente_id      INTEGER ,
    detalle_venta   VARCHAR(50),
    monto_neto      INTEGER ,
    monto_iva       INTEGER ,
    monto_total     INTEGER ,
    fecha           DATE ,
	cod_pago        INTEGER
);

CREATE TABLE PAGO
(
    estado          BOOLEAN,
    cod_pago        INTEGER 
);

CREATE TABLE EMPLEADO
(
    empleado_id     INTEGER PRIMARY KEY,
	nombre          VARCHAR(30),
	apellido        VARCHAR(30),
	rut             VARCHAR(30),
	sueldo          INTEGER
);

CREATE TABLE RESPALDO_BOLETA
(
	cliente_id      INTEGER ,
    detalle_venta   VARCHAR(50),
    monto_neto      INTEGER ,
    monto_iva       INTEGER ,
    monto_total     INTEGER ,
    fecha           DATE ,
	cod_pago        INTEGER
);

CREATE TABLE RESPALDO_FACTURA
(
	proveedor_id    INTEGER,
    producto_id     INTEGER,
    tipo_producto   VARCHAR(30),
    monto_total     INTEGER 
);

CREATE TABLE RESPALDO_DESPACHO
(
	despacho_id   INTEGER,
    fecha         DATE,
    hora_salida   TIME,
    hora_entrega  TIME,
    cliente_id    INTEGER,
    empleado_id   INTEGER 
);

ALTER TABLE despacho add foreign key (cliente_id) references cliente(cliente_id) on delete cascade;
ALTER TABLE despacho add foreign key (empleado_id) references empleado(empleado_id) on delete cascade;
ALTER TABLE boleta add foreign key(cliente_id) references cliente(cliente_id) on delete cascade;
ALTER TABLE boleta add foreign key(cod_pago) references pedido(cod_pago) on delete cascade;
ALTER TABLE proveedor add foreign key(producto_id) references producto(producto_id) on delete cascade;
ALTER TABLE factura add foreign key(proveedor_id) references proveedor(proveedor_id) on delete cascade;
ALTER TABLE factura add foreign key(producto_id) references producto(producto_id) on delete cascade;
ALTER TABLE pedido add foreign key(cliente_id) references cliente(cliente_id) on delete cascade;
ALTER TABLE pago add foreign key(cod_pago) references pedido(cod_pago) on delete cascade;
ALTER TABLE pedido add foreign key(producto_id) references producto(producto_id) on delete cascade;

select * from factura;
