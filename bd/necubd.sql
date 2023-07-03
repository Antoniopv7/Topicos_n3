CREATE SEQUENCE cliente_id
    minvalue 1
	increment by 1;

CREATE SEQUENCE despacho_id
    minvalue 1
	increment by 1;

CREATE SEQUENCE producto_id
    minvalue 1
	increment by 1;

CREATE SEQUENCE cod_pago
    minvalue 1
	increment by 1;

CREATE SEQUENCE proveedor_id
    minvalue 1
	increment by 1;

CREATE SEQUENCE empleado_id
    minvalue 1
	increment by 1;

CREATE TABLE CLIENTE
(
    cliente_id INTEGER DEFAULT nextval('cliente_id') PRIMARY KEY,
    nombre     VARCHAR (30),
    apellido   VARCHAR (30),
    rut        VARCHAR (30),
    direccion  VARCHAR (30),
    telefono   INTEGER
);

CREATE TABLE DESPACHO
(
    despacho_id   INTEGER DEFAULT nextval('despacho_id') PRIMARY KEY ,
    fecha         DATE,
    hora_salida   TIME,
    hora_entrega  TIME,
    cliente_id    INTEGER not null,
    empleado_id   INTEGER not null
);

CREATE TABLE PRODUCTO
( 
    producto_id INTEGER DEFAULT nextval('producto_id') PRIMARY KEY,
	nombre      VARCHAR(30) ,
    descripcion VARCHAR(30),
    valor       INTEGER  ,
    stock       INTEGER 
);

CREATE TABLE PEDIDO
(
    cod_pago       INTEGER DEFAULT nextval('cod_pago') PRIMARY KEY,
    fecha          DATE,
    monto_total    INTEGER,
    cliente_id     INTEGER not null
);

CREATE TABLE FACTURA
(
    proveedor_id    INTEGER NOT NULL,
    producto_id     INTEGER NOT NULL,
    tipo_producto   VARCHAR(30),
    monto_total     INTEGER 
);

CREATE TABLE PROVEEDOR 
(
    proveedor_id    INTEGER DEFAULT nextval('proveedor_id')PRIMARY KEY,
    producto_id     INTEGER NOT NULL
);

CREATE TABLE BOLETA
(
    cliente_id      INTEGER NOT NULL,
    detalle_venta   VARCHAR(50),
    monto_neto      INTEGER ,
    monto_iva       INTEGER ,
    monto_total     INTEGER ,
    fecha           DATE ,
	cod_pago        INTEGER NOT NULL
);

CREATE TABLE PAGO
(
    estado          BOOLEAN NOT NULL,
	monto_total     INTEGER,
    cod_pago        INTEGER NOT NULL
);

CREATE TABLE EMPLEADO
(
    empleado_id     INTEGER DEFAULT nextval('empleado_id') PRIMARY KEY,
	nombre          VARCHAR(30),
	apellido        VARCHAR(30),
	rut             VARCHAR(30),
	sueldo          INTEGER
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