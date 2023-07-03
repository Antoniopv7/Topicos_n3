import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import psycopg2

root = Tk()
root.title("Necu BD")

canvas = Canvas(root, height=300, width=1700)
canvas.pack()

frame = Frame()
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

# Funciones guardar

def Guardar_nuevo_cliente(nombre, apellido, rut, direccion, telefono):
    # Verificar que no hay datos nulos
    if not nombre or not apellido or not rut or not direccion or not telefono:
        showerror("Error", "Todos los campos deben ser llenados.")
        return

    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )    
        cursor = conn.cursor()        
        # Llamar al procedimiento almacenado insertar_cliente
        cursor.execute("CALL insertar_cliente(%s, %s, %s, %s, %s)", (nombre, apellido, rut, direccion, telefono))        
        conn.commit()
        showinfo("Necu BD", "Datos Insertados")                
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
    finally:
        if cursor is not None:
            cursor.close()        
        if conn is not None:
            conn.close()

def Guardar_nuevo_empleado(nombre, apellido, rut, sueldo):
    # Verificar que no hay datos nulos
    if not nombre or not apellido or not rut or not sueldo:
        showerror("Error", "Todos los campos deben ser llenados.")
        return

    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )    
        cursor = conn.cursor()        
        # Llamar al procedimiento almacenado insertar_empleado
        cursor.execute("CALL insertar_empleado(%s, %s, %s, %s)", (nombre, apellido, rut, sueldo))        
        conn.commit()
        showinfo("Necu BD", "Datos Insertados")                
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
    finally:
        if cursor is not None:
            cursor.close()        
        if conn is not None:
            conn.close()

def Guardar_nuevo_producto(nombre, descripcion, valor, stock):
    # Verificar que no hay datos nulos
    if not nombre or not descripcion or not valor or not stock:
        showerror("Error", "Todos los campos deben ser llenados.")
        return

    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )
        cursor = conn.cursor()
        # Llamar al procedimiento almacenado insertar_producto
        cursor.execute("CALL insertar_producto(%s, %s, %s, %s)", (nombre, descripcion, valor, stock))
        conn.commit()
        showinfo("Necu BD", "Datos Insertados")
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def Guardar_nuevo_proveedor(producto_id):
    # Verificar que no hay datos nulos
    if not producto_id:
        showerror("Error", "El id del producto no puede ser nulo.")
        return
    
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )
        cursor = conn.cursor()
        # Llamar al procedimiento almacenado insertar_proveedor
        cursor.execute("CALL insertar_proveedor(%s)", (producto_id,))
        conn.commit()
        showinfo("Necu BD", "Datos Insertados")
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def guardar_nueva_boleta(cliente_id, detalle_venta, monto_neto, monto_iva, monto_total, fecha, cod_pago):
    # Verificar que no hay datos nulos
    if not cliente_id or not detalle_venta or not monto_neto or not monto_iva or not monto_total or not fecha or not cod_pago:
        showerror("Error", "Todos los campos deben ser llenados.")
        return

    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )
        cursor = conn.cursor()
        # Llamar al procedimiento almacenado insertar_boleta
        cursor.execute("CALL insertar_boleta(%s,%s,%s,%s,%s,%s,%s)", (cliente_id, detalle_venta, monto_neto, monto_iva, monto_total, fecha, cod_pago))
        conn.commit()
        showinfo("Necu BD", "Datos Insertados")
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def Guardar_nuevo_pedido(fecha, total, cliente_id):
    # Verificar que no hay datos nulos
    if not fecha or not total or not cliente_id:
        showerror("Error", "Todos los campos deben ser llenados.")
        return
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )
        cursor = conn.cursor()
        # Llamar al procedimiento almacenado insertar_pedido
        cursor.execute("CALL insertar_pedido(%s,%s,%s)", (fecha, total, cliente_id))
        conn.commit()
        showinfo("Necu BD", "Datos Insertados")
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def Guardar_nuevo_despacho(fecha,hora_salida,hora_entrega,cliente_id,empleado_id):
    if not fecha or not hora_salida or not hora_entrega or not cliente_id or not empleado_id:
        showerror("Error", "Todos los campos deben ser llenados.")
        return
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )
        cursor = conn.cursor()
        # Llamar al procedimiento almacenado insertar_despacho
        cursor.execute("CALL inserta_despacho(%s,%s,%s,%s,%s)", (fecha,hora_salida,hora_entrega,cliente_id,empleado_id))
        conn.commit()
        showinfo("Necu BD",
        "Datos Insertados")
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
    finally:
        if cursor:
            cursor.close()
        if cursor:
            conn.close()

def Guardar_nuevo_pago(estado,monto_total,cod_pago):
    if not estado or not monto_total or not cod_pago:
        showerror("Error", "Todos los campos deben ser llenados.")
        return
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )
        cursor = conn.cursor()
        # Llamar al procedimiento almacenado insertar_pago
        cursor.execute("CALL insertar_pago(%s,%s,%s)", (estado,monto_total,cod_pago))
        conn.commit()
        showinfo("Necu BD",
        "Datos Insertados")
    except (Exception, psycopg2.DatabaseError)as error:
        showerror("Error", error)
        if cursor:
            cursor.close()
        if cursor:
            conn.close()

def Guardar_nuevo_factura(proveedor_id,producto_id,tipo_producto,monto_total):
    if not proveedor_id or not producto_id or not tipo_producto or not monto_total:
        showerror("Error", "Todos los campos deben ser llenados.")
        return
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Antonivan0',
            database='necubd'
        )
        cursor = conn.cursor()
        # Llamar al procedimiento almacenado insertar_factura
        cursor.execute("CALL insertar_factura(%s,%s,%s,%s)", (proveedor_id,producto_id,tipo_producto,monto_total))
        conn.commit()
        showinfo("Necu BD",
        "Datos Insertados")
    except(Exception, psycopg2.DatabaseError) as error:
        showerror("Error", error)
        if cursor:
            cursor.close()
        if cursor:
            conn.close()

# Funciones guardar

# Funciones Mostrar

def mostrar_boletas(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT * FROM boleta ORDER BY cod_pago'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_despachosxdespachador(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT nombre, COUNT(*) "Cantidad Despachos" FROM empleado JOIN despacho USING (empleado_id) GROUP BY nombre'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_ventas_dias(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT fecha, COUNT(*) "Ventas día" FROM pedido GROUP BY fecha ORDER BY fecha;'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_cliente_frecuente(x): ##considerando que en necu con más de 10 compras se vuelve cliente frecuente
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'select count (b.cliente_id), cl.nombre from boleta b join cliente cl using (cliente_id)group by cl.nombre having count (b.cliente_id) > 10;'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_boletasxcliente(x):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'select count (b.cliente_id), cl.nombre from boleta b join cliente cl using (cliente_id) group by cl.nombre;'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(x, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_producto(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT producto_id,nombre FROM producto join proveedor using(producto_id) ORDER BY producto_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=4,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_producto2(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT producto_id,nombre FROM producto join proveedor using(producto_id) ORDER BY producto_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_proveedor(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT proveedor_id,nombre FROM producto join proveedor using(producto_id) ORDER BY producto_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=0)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_cod_pago(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT cod_pago FROM pago ORDER BY cod_pago'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=2)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_cod_pago2(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT cod_pago FROM pago ORDER BY cod_pago'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_cliente(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT cliente_id FROM cliente ORDER BY cliente_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_cliente2(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT cliente_id FROM cliente ORDER BY cliente_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=2)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_empleado(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT empleado_id FROM empleado ORDER BY empleado_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=0)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_empleado2(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT empleado_id FROM empleado ORDER BY empleado_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_pedido(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT cod_pago FROM pedido ORDER BY cod_pago'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_pedido1(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT cod_pago FROM pedido ORDER BY cod_pago'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=0)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_despacho(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT despacho_id FROM despacho ORDER BY despacho_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_id_proveedor2(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT proveedor_id FROM proveedor ORDER BY proveedor_id'
    cursor.execute(query)
    row=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    listbox=Listbox(v3, width=20, height=5)
    listbox.grid(row=10,columnspan=1,column=1)

    for x in row:
        listbox.insert(END, x)

def mostrar_clientes(v3):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT * FROM cliente ORDER BY cliente_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v3, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

def mostrar_empleados(v5):
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor=conn.cursor()
    query= 'SELECT * FROM empleado ORDER BY empleado_id'
    cursor.execute(query)

    row=cursor.fetchall()

    listbox=Listbox(v5, width=50, height=10)
    listbox.grid(row=20,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    cursor.close()
    conn.close()

# Funciones Mostrar

# Funciones Buscar

def buscar_cliente(cliente_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'SELECT * FROM cliente WHERE cliente_id=%s'
    cursor.execute(query, (cliente_id))

    row=cursor.fetchall()

    listbox = Listbox(frame, width=40, height=1)
    listbox.grid(columnspan=4,column=30)

    for x in row:
        listbox.insert(END,x)

    conn.commit()
    cursor.close()
    conn.close()

# Funciones Buscar

# Funciones Eliminar 

from tkinter import messagebox

def eliminar_cliente(cliente_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    try:
        cursor.execute('CALL eliminar_cliente(%s)', (cliente_id,))
        conn.commit()
        showinfo("Necu BD",
        "Datos Eliminados")
    except psycopg2.errors.RaiseException as error:
        if 'no encontrado' in str(error):
            showerror("Error", "Está intentando eliminar un cliente que no existe.")
        else:
            showerror("Error al eliminar el cliente: ", error)
    except ValueError as ve:
        showwarning("Error", str(ve))
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error inesperado: ", error)
    finally:
        cursor.close()
        conn.close()

def eliminar_empleado(empleado_id):
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Antonivan0',
        database='necubd'
    )
    cursor = conn.cursor()
    try:
        cursor.execute('CALL eliminar_empleado(%s)', (empleado_id,))
        conn.commit()
        showinfo("Necu BD", "Datos Eliminados")
    except psycopg2.errors.RaiseException as error:
        if 'no encontrado' in str(error):
            showerror("Error", "Está intentando eliminar un empleado que no existe.")
        else:
            showerror("Error al eliminar el empleado: ", error)
    except ValueError as ve:
        showwarning("Error", str(ve))
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error inesperado: ", error)
    finally:
        cursor.close()
        conn.close()


def eliminar_despacho(despacho_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    try:
        cursor.execute('CALL eliminar_despacho(%s)', (despacho_id,))
        conn.commit()
        showinfo("Necu BD", "Datos Eliminados")
    except psycopg2.errors.RaiseException as error:
        if 'no encontrado' in str(error):
            showerror("Error", "Está intentando eliminar un despacho que no existe.")
        else:
            showerror("Error al eliminar el despacho: ", error)
    except ValueError as ve:
        showwarning("Error", str(ve))
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error inesperado: ", error)
    finally:
        cursor.close()
        conn.close()

def eliminar_pago(cod_pago):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    try:
        cursor.execute('CALL eliminar_pago(%s)', (cod_pago,))
        conn.commit()
        showinfo("Necu BD", "Datos Eliminados")
    except psycopg2.errors.RaiseException as error:
        if 'no encontrado' in str(error):
            showerror("Error", "Está intentando eliminar un pago que no existe.")
        else:
            showerror("Error al eliminar el pago: ", error)
    except ValueError as ve:
        showwarning("Error", str(ve))
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error inesperado: ", error)
    finally:
        cursor.close()
        conn.close()

def eliminar_producto(producto_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    try:
        cursor.execute('CALL eliminar_producto(%s)', (producto_id,))
        conn.commit()
        showinfo("Necu BD", "Datos Eliminados")
    except psycopg2.errors.RaiseException as error:
        if 'no encontrado' in str(error):
            showerror("Error", "Está intentando eliminar un producto que no existe.")
        else:
            showerror("Error al eliminar el producto: ", error)
    except ValueError as ve:
        showwarning("Error", str(ve))
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error inesperado: ", error)
    finally:
        cursor.close()
        conn.close()

def eliminar_proveedor(proveedor_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    try:
        cursor.execute('CALL eliminar_proveedor(%s)', (proveedor_id,))
        conn.commit()
        showinfo("Necu BD", "Datos Eliminados")
    except psycopg2.errors.RaiseException as error:
        if 'no encontrado' in str(error):
            showerror("Error", "Está intentando eliminar un proveedor que no existe.")
        else:
            showerror("Error al eliminar el proveedor: ", error)
    except ValueError as ve:
        showwarning("Error", str(ve))
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error inesperado: ", error)
    finally:
        cursor.close()
        conn.close()

def eliminar_pedido(codigo_ped):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    try:
        cursor.execute('CALL eliminar_pedido(%s)', (codigo_ped,))
        conn.commit()
        showinfo("Necu BD", "Datos Eliminados")
    except psycopg2.errors.RaiseException as error:
        if 'no encontrado' in str(error):
            showerror("Error", "Está intentando eliminar un pedido que no existe.")
        else:
            showerror("Error al eliminar el pedido: ", error)
    except ValueError as ve:
        showwarning("Error", str(ve))
    except (Exception, psycopg2.DatabaseError) as error:
        showerror("Error inesperado: ", error)
    finally:
        cursor.close()
        conn.close()


# Funciones Eliminar

# Funciones Modificar

def modificar_despacho(fecha,hora_salida,hora_entrega,cliente_id,empleado_id,despacho_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'UPDATE despacho SET fecha=%s,hora_salida=%s, hora_entrega=%s, cliente_id=%s, empleado_id=%s  WHERE despacho_id=%s'
    datos=(fecha,hora_salida,hora_entrega,cliente_id,empleado_id,despacho_id)
    cursor.execute(query,datos)
    conn.commit()
    showinfo("Necu BD",
    "Datos Modificados")
    conn.close() 
    cursor.close()

def modificar_pago(estado, cof_pago):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'UPDATE pago SET estado=%s  WHERE cod_pago=%s'
    datos=(estado, cof_pago)
    cursor.execute(query,datos)
    conn.commit()
    showinfo("Necu BD",
    "Datos Modificados")
    conn.close()
    cursor.close()

def modificar_cliente(nombre,apellido,rut,direccion,telefono,id_cliente):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'UPDATE cliente SET nombre=%s,apellido=%s,rut=%s,direccion=%s,telefono=%s WHERE cliente_id=%s'
    datos=(nombre,apellido,rut,direccion,telefono,id_cliente)
    cursor.execute(query,datos)
    conn.commit()
    showinfo("Necu BD",
    "Datos Modificados")
    conn.close()
    cursor.close()

def modificar_pedido(fecha,total,cliente_id,cod_pago):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'UPDATE pedido SET fecha=%s,total=%s,cliente_id=%s WHERE cod_pago=%s'
    datos=(fecha,total,cliente_id,cod_pago)
    cursor.execute(query,datos)
    conn.commit()
    showinfo("Necu BD",
    "Datos Modificados")
    conn.close()
    cursor.close()

def modificar_empleado(nombre,apellido,rut,sueldo, id_empleado):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'UPDATE empleado SET nombre=%s,apellido=%s,rut=%s,sueldo=%s WHERE empleado_id=%s'
    datos=(nombre,apellido,rut,sueldo, id_empleado)
    cursor.execute(query,datos)
    conn.commit()
    showinfo("Necu BD",
    "Datos Modificados")
    conn.close()
    cursor.close()

def modificar_proveedor(producto_id, proveedor_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'UPDATE proveedor SET producto_id=%s WHERE proveedor_id=%s'
    datos=(producto_id, proveedor_id)
    cursor.execute(query,datos)
    conn.commit()
    showinfo("Necu BD",
    "Datos Modificados")
    conn.close()
    cursor.close()

def modificar_producto(nombre,descripción,valor,stock, producto_id):
    conn = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'Antonivan0',
        database = 'necubd'
    )
    cursor = conn.cursor()
    query = 'UPDATE producto SET nombre=%s,descripcion=%s,valor=%s,stock=%s WHERE producto_id=%s'
    datos=(nombre,descripción,valor,stock, producto_id)
    cursor.execute(query,datos)
    conn.commit()
    showinfo("Necu BD",
    "Datos Modificados")
    conn.close()
    cursor.close()

# Funciones Modificar

#Ventanas

def ventana2():
    v2=Toplevel()
    v2.geometry("300x200")
    v2.title("Insertar datos")
    espacio1=Label(v2,text="Cliente").grid(row=0,column=0)
    label1 = Label(v2,text="Ingrese Nombre: ").grid(row=1,column=0)
    label2 = Label(v2,text="Ingrese apellido: ").grid(row=2,column=0)
    label3 = Label(v2,text="Ingrese rut: ").grid(row=3,column=0)
    label4 = Label(v2,text="Ingrese direccion: ").grid(row=4,column=0)
    label5 = Label(v2,text="Ingrese telefono: ").grid(row=5,column=0)
    espacio2 = Label(v2).grid(row=6,column=0)
    espacio3 = Label(v2).grid(row=7,column=0)
    espacio4 = Label(v2).grid(row=0,column=1)
    espacio5 = Label(v2).grid(row=6,column=1)
    espacio6 = Label(v2).grid(row=7,column=1)
    entry_nom = Entry(v2)
    entry_nom.grid(row=1,column=1)
    entry_ape = Entry(v2)
    entry_ape.grid(row=2,column=1)
    entry_rut = Entry(v2)
    entry_rut.grid(row=3,column=1)
    entry_dir = Entry(v2)
    entry_dir.grid(row=4,column=1)
    entry_tel = Entry(v2)
    entry_tel.grid(row=5,column=1)  

    boton_guardar_cliente = Button(v2,text="Guardar cliente",command=lambda:(Guardar_nuevo_cliente(
        entry_nom.get(),
        entry_ape.get(),
        entry_rut.get(),
        entry_dir.get(),
        entry_tel.get()
    ),v2.destroy()))
    boton_guardar_cliente.grid(row=6,column=1)

def ventana3():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Lista de clientes")
    labelv3 = Label(v3,text="| Id || Nombre || Apellido || Rut || Direccion || Telefono |").grid(row=0,column=0)
    mostrar_clientes(v3)

def ventana4():
    v4 = Toplevel()
    v4.geometry("300x200")
    v4.title("Insertar Datos")
    espacio1=Label(v4,text="Empleado").grid(row=0,column=0)
    label1 = Label(v4,text="Ingrese Nombre: ").grid(row=1,column=0)
    label2 = Label(v4,text="Ingrese Apellido: ").grid(row=2,column=0)
    label3 = Label(v4,text="Ingrese Rut: ").grid(row=3,column=0)
    label4 = Label(v4,text="Ingrese Sueldo: ").grid(row=4,column=0)
    espacio2 = Label(v4).grid(row=6,column=0)
    espacio3 = Label(v4).grid(row=7,column=0)
    espacio4 = Label(v4).grid(row=0,column=1)
    espacio5 = Label(v4).grid(row=6,column=1)
    espacio6 = Label(v4).grid(row=7,column=1)
    entry_nom = Entry(v4)
    entry_nom.grid(row=1,column=1)
    entry_ape = Entry(v4)
    entry_ape.grid(row=2,column=1)
    entry_rut = Entry(v4)
    entry_rut.grid(row=3,column=1)
    entry_sue = Entry(v4)
    entry_sue.grid(row=4,column=1)

    boton_guardar_empleado = Button(v4,text="Guardar Empleado",command=lambda:(Guardar_nuevo_empleado(
        entry_nom.get(),
        entry_ape.get(),
        entry_rut.get(),
        entry_sue.get()
        ),v4.destroy()))
    boton_guardar_empleado.grid(row=5,column=1)

def ventana5():
    v5 = Toplevel()
    v5.geometry("300x200")
    v5.title("Lista de clientes")
    labelv5 = Label(v5,text="| Id || Nombre || Apellido || Rut || Sueldo |").grid(row=0,column=0)
    mostrar_empleados(v5)

def ventana6():
    v6 = Toplevel()
    v6.geometry("300x200")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Producto").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Nombre: ").grid(row=1,column=0)
    label2 = Label(v6,text="Ingrese Descripcion: ").grid(row=2,column=0)
    label3 = Label(v6,text="Ingrese Valor: ").grid(row=3,column=0)
    label4 = Label(v6,text="Ingrese Stock: ").grid(row=4,column=0)
    espacio2 = Label(v6).grid(row=6,column=0)
    espacio3 = Label(v6).grid(row=7,column=0)
    espacio4 = Label(v6).grid(row=0,column=1)
    espacio5 = Label(v6).grid(row=6,column=1)
    espacio6 = Label(v6).grid(row=7,column=1)
    entry_nom = Entry(v6)
    entry_nom.grid(row=1,column=1)
    entry_des = Entry(v6)
    entry_des.grid(row=2,column=1)
    entry_val = Entry(v6)
    entry_val.grid(row=3,column=1)
    entry_sto = Entry(v6)
    entry_sto.grid(row=4,column=1)

    boton_guardar_producto = Button(v6,text="Guardar Producto",command=lambda:(Guardar_nuevo_producto(
        entry_nom.get(),
        entry_des.get(),
        entry_val.get(),
        entry_sto.get()
        ),v6.destroy()))
    boton_guardar_producto.grid(row=5,column=1)

def ventana7():
    v6 = Toplevel()
    v6.geometry("300x200")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Proveedor").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Id_producto: ").grid(row=1,column=0)
    
    id_prod = Entry(v6)
    id_prod.grid(row=1,column=1)
    mostrar_id_producto(v6)


    boton_guardar = Button(v6,text="Guardar Proveedor",command=lambda:(Guardar_nuevo_proveedor(id_prod.get()),v6.destroy()))
    boton_guardar.grid(row=2,column=1)

def ventana8():
    v6 = Toplevel()
    v6.geometry("400x600")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Factura").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Id del proveedor: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese Id del producto: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese el codigo: ").grid(row=3,column=0)
    label1 = Label(v6,text="Ingrese el tipo de producto: ").grid(row=3,column=0)
    label1 = Label(v6,text="Ingrese el monto total: ").grid(row=4,column=0)
    proveedor_id = Entry(v6)
    proveedor_id.grid(row=1,column=1)
    producto_id = Entry(v6)
    producto_id.grid(row=2,column=1)
    tipo_producto = Entry(v6)
    tipo_producto.grid(row=3,column=1)
    monto_total = Entry(v6)
    monto_total.grid(row=4,column=1)
    label1 = Label(v6,text="| Id_producto || Nombre |").grid(row=9,column=1)
    mostrar_id_producto2(v6)
    label1 = Label(v6,text="| Id_provedor || Nombre |").grid(row=9,column=0)
    mostrar_id_proveedor(v6)


    boton_guardar = Button(v6,text="Guardar Factura",command=lambda:(Guardar_nuevo_factura(
        proveedor_id.get(), 
        producto_id.get(),
        tipo_producto.get(), 
        monto_total.get()
        ),v6.destroy()))
    boton_guardar.grid(row=6,column=1)

def ventana9():
    v6 = Toplevel()
    v6.geometry("400x300")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Boleta").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Id_Cliente: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese Detalle de la venta: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese Monto neto: ").grid(row=3,column=0)
    label1 = Label(v6,text="Ingrese Monto iva: ").grid(row=4,column=0)
    label1 = Label(v6,text="Ingrese Monto total: ").grid(row=5,column=0)
    label1 = Label(v6,text="Ingrese Fecha: ").grid(row=6,column=0)
    label1 = Label(v6,text="Ingrese Codigo del pago: ").grid(row=7,column=0)
    
    cliente_id = Entry(v6)
    cliente_id.grid(row=1,column=1)
    detalle_venta = Entry(v6)
    detalle_venta.grid(row=2,column=1)
    monto_neto = Entry(v6)
    monto_neto.grid(row=3,column=1)
    monto_iva = Entry(v6)
    monto_iva.grid(row=4,column=1)
    monto_total = Entry(v6)
    monto_total.grid(row=5,column=1)
    fecha = Entry(v6)
    fecha.grid(row=6,column=1)
    cod_pago = Entry(v6)
    cod_pago.grid(row=7,column=1)

    label1= Label(v6,text="| Cod_pago |").grid(row=9,column=2)
    label1= Label(v6,text="| Id_cliente |").grid(row=9,column=1)
    mostrar_cod_pago(v6)
    mostrar_id_cliente(v6)
    
    boton_guardar = Button(v6,text="Guardar Boleta",command=lambda:(guardar_nueva_boleta(
        cliente_id.get(),
        detalle_venta.get(),
        monto_neto.get(),
        monto_iva.get(),
        monto_total.get(), 
        fecha.get(), 
        cod_pago.get()
        ),v6.destroy()))
    boton_guardar.grid(row=8,column=1)

def ventana10():
    v6 = Toplevel()
    v6.geometry("300x200")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="pago").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese Estado del pago: ").grid(row=1,column=0)
    label2 = Label(v6,text="Ingrese Monto Total: ").grid(row=2,column=0)
    label2 = Label(v6,text="Ingrese codigo de pago: ").grid(row=3,column=0)
    
    estado = Entry(v6)
    estado.grid(row=1,column=1)

    Monto = Entry(v6)
    Monto.grid(row=2,column=1)

    cod = Entry(v6)
    cod.grid(row=3,column=1)
    
    boton_guardar = Button(v6,text="Guardar Pago",command=lambda:(Guardar_nuevo_pago(estado.get(), Monto.get(), cod.get()),v6.destroy()))
    boton_guardar.grid(row=8,column=1)
    mostrar_cod_pago2(v6)

def ventana11():
    v6 = Toplevel()
    v6.geometry("400x300")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Pedido").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese fecha pedido: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese el monto total del pedido: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese el ID del cliente : ").grid(row=3,column=0)   
    fecha = Entry(v6)
    fecha.grid(row=1,column=1)
    total = Entry(v6)
    total.grid(row=2,column=1)
    cliente_id = Entry(v6)
    cliente_id.grid(row=3,column=1)
    label1= Label(v6,text="| Id_cliente |").grid(row=9,column=1)
    mostrar_id_cliente(v6)
    
    boton_guardar = Button(v6,text="Guardar Pedido",command=lambda:(Guardar_nuevo_pedido(
        fecha.get(), 
        total.get(), 
        cliente_id.get()),v6.destroy()))
    boton_guardar.grid(row=4,column=1)

def ventana12():
    v6 = Toplevel()
    v6.geometry("450x300")
    v6.title("Insertar Datos")
    espacio1=Label(v6,text="Despacho").grid(row=0,column=0)
    label1 = Label(v6,text="Ingrese la fecha del despacho: ").grid(row=1,column=0)
    label1 = Label(v6,text="Ingrese la hora de salida del despacho: ").grid(row=2,column=0)
    label1 = Label(v6,text="Ingrese la hora de entrega del despacho: ").grid(row=3,column=0)
    label1 = Label(v6,text="Ingrese el id del cliente asociado al despacho: ").grid(row=4,column=0)
    label1 = Label(v6,text="Ingrese el id del empleado asociado al despacho: ").grid(row=5,column=0)
    
    fecha = Entry(v6)
    fecha.grid(row=1,column=1)
    hora_salida = Entry(v6)
    hora_salida.grid(row=2,column=1)
    hora_entrega = Entry(v6)
    hora_entrega.grid(row=3,column=1)
    cliente_id = Entry(v6)
    cliente_id.grid(row=4,column=1)
    empleado_id = Entry(v6)
    empleado_id.grid(row=5,column=1)
    mostrar_id_cliente(v6)
    mostrar_id_empleado(v6)
    label1 = Label(v6,text="| Id_cliente |").grid(row=7,column=1)
    label1 = Label(v6,text="| Id_empleado |").grid(row=7,column=0)
    
    boton_guardar = Button(v6,text="Guardar Despacho",command=lambda:(Guardar_nuevo_despacho(
        fecha.get(), 
        hora_salida.get(), 
        hora_entrega.get(), 
        cliente_id.get(), 
        empleado_id.get()
        ),v6.destroy()))
    boton_guardar.grid(row=6,column=1)

def ventana13():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Despachos por despachador")
    labelv3 = Label(v3,text="| Nombre || Cantidad de despachos |").grid(row=0,column=0)
    mostrar_despachosxdespachador(v3)

def ventana14():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Ventas por dia")
    labelv3 = Label(v3,text="| Fecha || Cantidad de ventas |").grid(row=0,column=0)
    mostrar_ventas_dias(v3)

def ventana16():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Clientes frecuentes")
    labelv3 = Label(v3,text="| Cantidad de compras || Nombre |").grid(row=0,column=0)
    mostrar_cliente_frecuente(v3)

def ventana17():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Listado de boletas")
    labelv3 = Label(v3,text="| Client id || Detalle venta || Monto neto || Monto iva || Monto total || fecha || Codigo de pago |").grid(row=0,column=0)
    mostrar_boletas(v3)

def ventana18():
    v3 = Toplevel()
    v3.geometry("350x200")
    v3.title("Eliminar cliente")
    labelv3 = Label(v3,text="Cliente").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el ID cliente a eliminar").grid(row=1,column=0)
    cliente = Entry(v3)
    cliente.grid(row=1,column=1)
    label = Label(v3,text="|Id Cliente|")
    mostrar_id_cliente(v3)

    boton_eliminar = Button(v3,text="Eliminar Cliente",command=lambda:(eliminar_cliente(cliente.get()),v3.destroy()))
    boton_eliminar.grid(row=2,column=1)

def ventana19():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Eliminar Empleado")
    labelv3 = Label(v3,text="Empleado").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el ID empleado a eliminar").grid(row=0,column=1)
    empleado = Entry(v3)
    empleado.grid(row=1,column=1)
    label = Label(v3,text="|Id Empleado|")
    mostrar_id_empleado2(v3)

    boton_eliminar = Button(v3,text="Eliminar Empleado",command=lambda:(eliminar_empleado(empleado.get()),v3.destroy()))
    boton_eliminar.grid(row=2,column=1)

def ventana20():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Eliminar Despacho")
    labelv3 = Label(v3,text="Despacho").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el ID despacho a eliminar").grid(row=0,column=1)
    despacho = Entry(v3)
    despacho.grid(row=1,column=1)
    label = Label(v3,text="|Id Despacho|")
    mostrar_id_despacho(v3)

    boton_eliminar = Button(v3,text="Eliminar Despacho",command=lambda:(eliminar_despacho(despacho.get()),v3.destroy()))
    boton_eliminar.grid(row=2,column=1)


def ventana21():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Eliminar Pago")
    labelv3 = Label(v3,text="Pago").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el código del pago a eliminar").grid(row=0,column=1)
    pago = Entry(v3)
    pago.grid(row=1,column=1)
    label = Label(v3,text="|Código Pago|")
    mostrar_cod_pago2(v3)

    boton_eliminar = Button(v3,text="Eliminar Pago",command=lambda:(eliminar_pago(pago.get()),v3.destroy()))
    boton_eliminar.grid(row=2,column=1)


def ventana22():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Eliminar Producto")
    labelv3 = Label(v3,text="Producto").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el ID producto a eliminar").grid(row=0,column=1)
    producto = Entry(v3)
    producto.grid(row=1,column=1)
    label = Label(v3,text="|Id Producto|")
    mostrar_id_producto(v3)

    boton_eliminar = Button(v3,text="Eliminar Producto",command=lambda:(eliminar_producto(producto.get()),v3.destroy()))
    boton_eliminar.grid(row=2,column=1)

def ventana23():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Eliminar Proveedor")
    labelv3 = Label(v3,text="Proveedor").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el ID proveedor a eliminar").grid(row=0,column=1)
    proveedor = Entry(v3)
    proveedor.grid(row=1,column=1)
    label = Label(v3,text="|Id Proveedor|")
    mostrar_id_proveedor2(v3)

    boton_eliminar = Button(v3,text="Eliminar Proveedor",command=lambda:(eliminar_proveedor(proveedor.get()),v3.destroy()))
    boton_eliminar.grid(row=2,column=1)


def ventana24():
    v3 = Toplevel()
    v3.geometry("300x200")
    v3.title("Eliminar Pedido")
    labelv3 = Label(v3,text="Pedido").grid(row=0,column=0)
    labelv3 = Label(v3,text="Ingrese el código de pedido a eliminar").grid(row=0,column=1)
    pedido = Entry(v3)
    pedido.grid(row=1,column=1)
    label = Label(v3,text="|Código Pedido|")
    mostrar_id_pedido(v3)

    boton_eliminar = Button(v3,text="Eliminar Pedido",command=lambda:(eliminar_pedido(pedido.get()),v3.destroy()))
    boton_eliminar.grid(row=2,column=1)

def ventana_m1():
    v3 = Toplevel()
    v3.geometry("400x300")
    v3.title("Modificar Cliente")
    labelv3 = Label(v3,text="Cliente").grid(row=0,column=0)
    labelv2 = Label(v3,text="Ingrese el ID cliente a Modificar: ").grid(row=1,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Nombre: ").grid(row=2,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Apellido: ").grid(row=3,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Rut: ").grid(row=4,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Direccion: ").grid(row=5,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Telefono: ").grid(row=6,column=0)
    id_cliente = Entry(v3)
    id_cliente.grid(row=1,column=1)
    nombre = Entry(v3)
    nombre.grid(row=2,column=1)
    apellido = Entry(v3)
    apellido.grid(row=3,column=1)
    rut = Entry(v3)
    rut.grid(row=4,column=1)
    direccion = Entry(v3)
    direccion.grid(row=5,column=1)
    telefono = Entry(v3)
    telefono.grid(row=6,column=1)
    label = Label(v3,text="|Id Cliente|")
    mostrar_id_cliente(v3)

    boton_modificar = Button(v3,text="Modificar Cliente",command=lambda:(modificar_cliente(
        nombre.get(), 
        apellido.get(), 
        rut.get(), 
        direccion.get(), 
        telefono.get(), 
        id_cliente.get()
        ),v3.destroy()))
    boton_modificar.grid(row=7,column=1)

def ventana_m2():
    v3 = Toplevel()
    v3.geometry("400x300")
    v3.title("Modificar Empleado")
    labelv3 = Label(v3,text="Empleado").grid(row=0,column=0)
    labelv2 = Label(v3,text="Ingrese el ID Empleado a Modificar: ").grid(row=1,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Nombre: ").grid(row=2,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Apellido: ").grid(row=3,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Rut: ").grid(row=4,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Sueldo: ").grid(row=5,column=0)
    empleado_id = Entry(v3)
    empleado_id.grid(row=1,column=1)
    nombre = Entry(v3)
    nombre.grid(row=2,column=1)
    apellido = Entry(v3)
    apellido.grid(row=3,column=1)
    rut = Entry(v3)
    rut.grid(row=4,column=1)
    sueldo = Entry(v3)
    sueldo.grid(row=5,column=1)
    label = Label(v3,text="|Id Empleado|").grid(row=7,column=0)
    mostrar_id_empleado(v3)

    boton_modificar = Button(v3,text="Modificar Empleado",command=lambda:(modificar_empleado(
        nombre.get(), 
        apellido.get(), 
        rut.get(), 
        sueldo.get(),
        empleado_id.get()
        ),v3.destroy()))
    boton_modificar.grid(row=6,column=1)


def ventana_m3():
    v3 = Toplevel()
    v3.geometry("500x300")
    v3.title("Modificar despacho")
    labelv3 = Label(v3,text="Despacho").grid(row=0,column=0)
    labelv2 = Label(v3,text="Ingrese el id de despacho a modificar: ").grid(row=1,column=0)
    labelv2 = Label(v3,text="Ingrese nueva fecha de despacho: ").grid(row=2,column=0)
    labelv2 = Label(v3,text="ingrese nueva hora_salida: ").grid(row=3,column=0)
    labelv2 = Label(v3,text="Ingrese nueva hora entrega: ").grid(row=4,column=0)
    labelv2 = Label(v3,text="ingrese nuevo cliente ID: ").grid(row=5,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo empleado ID: ").grid(row=6,column=0)

    despacho_id = Entry(v3)
    despacho_id.grid(row=1,column=1)
    fecha = Entry(v3)
    fecha.grid(row=2,column=1)
    hora_salida = Entry(v3)
    hora_salida.grid(row=3,column=1)
    hora_entrega = Entry(v3)
    hora_entrega.grid(row=4,column=1)
    cliente_id = Entry(v3)
    cliente_id.grid(row=5,column=1)
    empleado_id = Entry(v3)
    empleado_id.grid(row=6,column=1)
    label = Label(v3,text="|Id despacho|").grid(row=8,column=1)
    mostrar_id_despacho(v3)
    label = Label(v3,text="|Id empleado|").grid(row=8,column=0)
    mostrar_id_empleado(v3)
    label = Label(v3,text="|Id cliente|").grid(row=8,column=2)
    mostrar_id_cliente2(v3)

    boton_modificar = Button(v3,text="Modificar Empleado",command=lambda:(modificar_despacho( 
        fecha.get(), 
        hora_salida.get(), 
        hora_entrega.get(), 
        cliente_id.get(), 
        empleado_id.get(),
        despacho_id.get()
        ),v3.destroy()))
    boton_modificar.grid(row=7,column=1) 

def ventana_m4():
    v3 = Toplevel()
    v3.geometry("600x300")
    v3.title("Modificar pago")
    labelv3 = Label(v3,text="pago").grid(row=0,column=0)
    labelv2 = Label(v3,text="Ingrese el codigo del pago que quiere modificar: ").grid(row=1,column=0)
    labelv2 = Label(v3,text="Ingrese nuevo estado del pago puede ser [Aprobado] o [EN ESPERA]: ").grid(row=2,column=0)
    cod_pago = Entry(v3)
    cod_pago.grid(row=1,column=1)
    estado = Entry(v3)
    estado.grid(row=2,column=1)
    label = Label(v3,text="|pago|").grid(row=4,column=1)
    mostrar_cod_pago2(v3)

    boton_modificar = Button(v3,text="Modificar pago",command=lambda:(modificar_pago(
        estado.get(),
        cod_pago.get()
        ),v3.destroy()))
    boton_modificar.grid(row=3,column=1)

def ventana_m5():
    v3 = Toplevel()
    v3.geometry("400x300")
    v3.title("Modificar Producto")
    labelv3 = Label(v3,text="Producto").grid(row=0,column=0)
    labelv2 = Label(v3,text="Ingrese el ID Producto a Modificar: ").grid(row=1,column=0)
    labelv2 = Label(v3,text="Ingrese nuevo nombre de Producto: ").grid(row=2,column=0)
    labelv2 = Label(v3,text="Ingrese nueva descripción de Producto: ").grid(row=3,column=0)
    labelv2 = Label(v3,text="Ingrese nuevo valor de Producto: ").grid(row=4,column=0)
    labelv2 = Label(v3,text="Ingrese nuevo stock de Producto: ").grid(row=5,column=0)
    producto_id = Entry(v3)
    producto_id.grid(row=1,column=1)
    nombre = Entry(v3)
    nombre.grid(row=2,column=1)
    descripcion = Entry(v3)
    descripcion.grid(row=3,column=1)
    valor = Entry(v3)
    valor.grid(row=4,column=1)
    stock = Entry(v3)
    stock.grid(row=5,column=1)
    label = Label(v3,text="|Id Producto|")
    mostrar_id_proveedor(v3)

    boton_modificar = Button(v3,text="Modificar Producto",command=lambda:(modificar_producto(

    nombre.get(),
    descripcion.get(),
    valor.get(),
    stock.get(),
    producto_id.get()

    ),v3.destroy()))
    boton_modificar.grid(row=7,column=1)

def ventana_m6():
    v3 = Toplevel()
    v3.geometry("400x300")
    v3.title("Modificar Proveedor")
    labelv3 = Label(v3,text="Proveedor").grid(row=0,column=0)
    labelv2 = Label(v3,text="Ingrese el ID proveedor a Modificar: ").grid(row=1,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo ID de Producto: ").grid(row=2,column=0)
    id_proveedor = Entry(v3)
    id_proveedor.grid(row=1,column=1)
    id_producto = Entry(v3)
    id_producto.grid(row=2,column=1)
    label = Label(v3,text="|Id Proveedor|").grid(row=4,column=0)
    mostrar_id_proveedor(v3)
    label = Label(v3,text="|Id Producto|").grid(row=4,column=1)
    mostrar_id_producto2(v3)

    boton_modificar = Button(v3,text="Modificar Proveedor",command=lambda:(modificar_proveedor(

    id_producto.get(),
    id_proveedor.get()
    ),v3.destroy()))
    boton_modificar.grid(row=3,column=1)

def ventana_m7():
    v3 = Toplevel()
    v3.geometry("400x300")
    v3.title("Modificar Pedido")
    labelv3 = Label(v3,text="Pedido").grid(row=0,column=0)
    labelv2 = Label(v3,text="Ingrese el código del pedido a Modificar: ").grid(row=1,column=0)
    labelv2 = Label(v3,text="Ingrese Nueva Fecha: ").grid(row=2,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Total: ").grid(row=3,column=0)
    labelv2 = Label(v3,text="Ingrese Nuevo Cliente_ID: ").grid(row=4,column=0)
    codigo = Entry(v3)
    codigo.grid(row=1,column=1)
    fecha = Entry(v3)
    fecha.grid(row=2,column=1)
    total = Entry(v3)
    total.grid(row=3,column=1)
    cliente_id = Entry(v3)
    cliente_id.grid(row=4,column=1)
    label = Label(v3,text="|Código|").grid(row=6,column=0)
    mostrar_id_pedido1(v3)
    label = Label(v3,text="|Cliente_id|").grid(row=6,column=1)
    mostrar_id_cliente(v3)

    boton_modificar = Button(v3,text="Modificar Pedido",command=lambda:(modificar_pedido(
        fecha.get(), 
        total.get(), 
        cliente_id.get(),
        codigo.get()
        ),v3.destroy()))
    boton_modificar.grid(row=5,column=1)

#Ventanas  

#label frame
cliente = Label(frame,text="Cliente").grid(row=0,column=0)
espacio = Label(frame).grid(row=0,column=1)
espacio = Label(frame).grid(row=0,column=2)
espacio = Label(frame).grid(row=1,column=1)
espacio = Label(frame).grid(row=1,column=2)
empleado = Label(frame,text="Empleado").grid(row=0,column=3)
espacio = Label(frame).grid(row=0,column=4)
espacio = Label(frame).grid(row=0,column=5)
espacio = Label(frame).grid(row=1,column=4)
espacio = Label(frame).grid(row=1,column=5)
producto = Label(frame,text="Producto").grid(row=0,column=6)
espacio = Label(frame).grid(row=0,column=7)
espacio = Label(frame).grid(row=0,column=8)
espacio = Label(frame).grid(row=1,column=7)
espacio = Label(frame).grid(row=1,column=8)
Proveedor = Label(frame,text="Proveedor").grid(row=0,column=9)
espacio = Label(frame).grid(row=0,column=10)
espacio = Label(frame).grid(row=0,column=11)
espacio = Label(frame).grid(row=1,column=10)
espacio = Label(frame).grid(row=1,column=11)
Factura = Label(frame,text="Factura").grid(row=0,column=12)
espacio = Label(frame).grid(row=0,column=13)
espacio = Label(frame).grid(row=0,column=14)
espacio = Label(frame).grid(row=1,column=13)
espacio = Label(frame).grid(row=1,column=14)
Boleta = Label(frame,text="Boleta").grid(row=0,column=15)
espacio = Label(frame).grid(row=0,column=16)
espacio = Label(frame).grid(row=1,column=17)
espacio = Label(frame).grid(row=1,column=16)
espacio = Label(frame).grid(row=1,column=17)
Pago = Label(frame,text="Pago").grid(row=0,column=18)
espacio = Label(frame).grid(row=0,column=19)
espacio = Label(frame).grid(row=1,column=20)
espacio = Label(frame).grid(row=1,column=19)
espacio = Label(frame).grid(row=1,column=20)
Pedido = Label(frame,text="Pedido").grid(row=0,column=21)
espacio = Label(frame).grid(row=0,column=22)
espacio = Label(frame).grid(row=1,column=23)
espacio = Label(frame).grid(row=1,column=22)
espacio = Label(frame).grid(row=1,column=23)
Despacho = Label(frame,text="Despacho").grid(row=0,column=24)
espacio = Label(frame).grid(row=2,column=0)
espacio = Label(frame).grid(row=2,column=3)
espacio = Label(frame).grid(row=2,column=24)
espacio = Label(frame).grid(row=2,column=21)
espacio = Label(frame).grid(row=2,column=12)
espacio = Label(frame).grid(row=2,column=18)
espacio = Label(frame).grid(row=2,column=15)
espacio = Label(frame).grid(row=4,column=0)
espacio = Label(frame).grid(row=6,column=0)
espacio = Label(frame).grid(row=6,column=3)
espacio = Label(frame).grid(row=6,column=24)
espacio = Label(frame).grid(row=6,column=21)
espacio = Label(frame).grid(row=6,column=6)
espacio = Label(frame).grid(row=6,column=18)
espacio = Label(frame).grid(row=6,column=9)
#label frame

#button frame
boton_v2 = Button(frame, text="Insertar cliente",command=lambda:ventana2()).grid(row=1,column=0)
boton_v4 = Button(frame, text="Insertar empleado",command=lambda:ventana4()).grid(row=1,column=3)
boton_v6 = Button(frame, text="Insertar Producto",command=lambda:ventana6()).grid(row=1,column=6)
boton_v7 = Button(frame, text="Insertar Proveedor",command=lambda:ventana7()).grid(row=1,column=9)
boton_v8 = Button(frame, text="Insertar Factura",command=lambda:ventana8()).grid(row=1,column=12)
boton_v9 = Button(frame, text="Insertar Boleta",command=lambda:ventana9()).grid(row=1,column=15)
boton_v10 = Button(frame, text="Insertar Pago",command=lambda:ventana10()).grid(row=1,column=18)
boton_v11 = Button(frame, text="Insertar Pedido",command=lambda:ventana11()).grid(row=1,column=21)
boton_v12 = Button(frame, text="Insertar Despacho",command=lambda:ventana12()).grid(row=1,column=24)


boton_v3 = Button(frame, text="Mostrar clientes",command=lambda:ventana3()).grid(row=3,column=0)
boton_v5 = Button(frame, text="Mostrar empleados",command=lambda:ventana5()).grid(row=3,column=3)
boton_v13 = Button(frame, text="Mostrar Despachos por despachador",command=lambda:ventana13()).grid(row=3,column=24)
boton_v14 = Button(frame, text="Mostrar Ventas por dia",command=lambda:ventana14()).grid(row=3,column=21)
boton_v16 = Button(frame, text="Cliente Frecuente",command=lambda:ventana16()).grid(row=3,column=18)
boton_v17 = Button(frame, text="Mostrar Listado de boletas",command=lambda:ventana17()).grid(row=3,column=15)
boton_v18 = Button(frame, text="Eliminar Cliente",command=lambda:ventana18()).grid(row=5,column=0)
boton_v19 = Button(frame, text="Eliminar Empleado",command=lambda:ventana19()).grid(row=5,column=3)
boton_v20 = Button(frame, text="Eliminar Despacho",command=lambda:ventana20()).grid(row=5,column=24)
boton_v21 = Button(frame, text="Eliminar Pago",command=lambda:ventana21()).grid(row=5,column=18)
boton_v22 = Button(frame, text="Eliminar Producto",command=lambda:ventana22()).grid(row=5,column=6)
boton_v23 = Button(frame, text="Eliminar Proveedor",command=lambda:ventana23()).grid(row=5,column=9)
boton_v24 = Button(frame, text="Eliminar Pedido",command=lambda:ventana24()).grid(row=5,column=21)
boton_mod1 = Button(frame, text="Modificar Cliente",command=lambda:ventana_m1()).grid(row=7,column=0)
boton_mod2 = Button(frame, text="Modificar Empleado",command=lambda:ventana_m2()).grid(row=7,column=3) 
boton_mod3 = Button(frame, text="Modificar Despacho",command=lambda:ventana_m3()).grid(row=7,column=24) 
boton_mod4 = Button(frame, text="Modificar Pago",command=lambda:ventana_m4()).grid(row=7,column=18) 
boton_mod5 = Button(frame, text="Modificar Producto",command=lambda:ventana_m5()).grid(row=7,column=6) 
boton_mod6 = Button(frame, text="Modificar Proveedor",command=lambda:ventana_m6()).grid(row=7,column=9) 
boton_mod7 = Button(frame, text="Modificar Pedido",command=lambda:ventana_m7()).grid(row=7,column=21) 
#button frame

root.mainloop()