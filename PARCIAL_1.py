import sqlite3

#Creamos la base de datos
conn = sqlite3.connect('InventarioProductos.db')


c = conn.cursor()

#Creamos la tabla que contiene los productos
c.execute("""CREATE TABLE if not exists Inventario(
            Id_Producto integer primary key AUTOINCREMENT,
            Producto text,
            Cantidad text,
            Proveedor text
            )""")
conn.commit()


#Definimos las funciones que aplicaran los requerimientos del programa

def insertar(a,b,con):
    c.execute("insert into Inventario(Producto,Cantidad,Proveedor) VALUES (?,?,?)", (a,b,con))
    conn.commit()

def eliminar(ProductoE):
    sentencia = "delete from  Inventario WHERE Producto = " + "'" + ProductoE + "'"
    c.execute(sentencia)
    conn.commit()
    print("El producto : ",ProductoE, "se ha eliminado correctamente de su base de datos ")

def mostrarDatos():
    c.execute("SELECT Id_Producto, Producto, Cantidad, Proveedor  from Inventario")
    rows = c.fetchall()
    for row in rows:
        print("\nId_Producto= ", row[0], "Producto = ", row[1], "Cantidad", row[2],"Proveedor", row[3] )

def buscar(ProductoB):
    sentencias = "select Id_Producto,Producto, Cantidad, Proveedor  from Inventario WHERE Producto = " + "'" + ProductoB + "'"       
    c.execute(sentencias)
    rows = c.fetchall()
    for row in rows:
        print("Id_Producto :",row[0]," Producto : ", row[1]," posee : ", row[2], " en existencia", " El proveedor es : ", row[3])

def editarcantidad(ProductoB,CantidadN):
    sentencia = "UPDATE Inventario SET Cantidad =" +"'" + CantidadN + "'" "WHERE Producto =" + "'" + ProductoB + "'"
    c.execute(sentencia)
    conn.commit()


#Una vez definidas todas las funciones le damos inicio al programa con un bucle While


print("Inicio del Programa Base de datos Inventario")

while True:
    Respuesta1 = input("Si desea agregar un Producto al inventario presione 1, de lo contrario presione otro valor : ")
    if Respuesta1 == "1":
        Respuesta11 = "1"
        while Respuesta11 == "1":
            a=input("Introduzca el Producto : ")
            b =input ("Introduzca la cantidad disponible : ")
            con =input ("Introduzca el proveedor : ")
            insertar(a,b,con)
            Respuesta11= input("Deseas agregar otra producto?, Si (1), No (2)")
            
    Respuesta2 = input("\nSi desea editar la cantidad disponible de un producto presione 1, de lo contrario presione otro valor : ")
    if Respuesta2 == "1":
        ProductoB = input("Introduzca el producto que  desee cambiarle la disponibilidad : ")
        CantidadN= (input("Introduzca la nueva cantidad de ese producto : "))
        editarcantidad(ProductoB,CantidadN)


    Respuesta3 = input("\nSi desea ver todas los productos de su base de datos presione 1, de lo contrario presione otro valor : ")
    if Respuesta3 == "1":
        mostrarDatos()
                
    Respuesta5 = input("\nSi desea ver algun producto en especifico presione 1, de lo contrario presione otro valor : ")
    if Respuesta5 == "1":
        productoB= input("\nIntroduzca el producto a buscar: ")
        buscar(productoB)
        
    Respuesta6 = input("\nSi desea eliminar algun producto de la base de datos presione 1, de lo contrario presione otro valor : ")
    if Respuesta6 == "1":
        productoE = input("\nIntroduzca el producto que desea eliminar : ")
        eliminar(productoE)
    
    Respuesta7 = input("\nSi desea salir del programa presione 1, de lo contrario presione otro valor : ")
    if Respuesta7 == "1":
        break
    
print("Fin del Programa")

conn.close()