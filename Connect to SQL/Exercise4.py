#Ejercicio 4: Escribir un script que pida al usuario que ingrese un ID de cliente. El script debe buscar y mostrar el nombre del cliente correspondiente a
#ese ID. Si el ID no existe, debe mostrar un mensaje de error

#Hola jijodebus 
#Import the library XD
import sqlite3

#Connecto to database 
conexion=sqlite3.connect("bd1.db")
id_cliente= int(input("Ingrese un ID de Cliente: "))
try:
    #Search the name with id_cliente
    cursor=conexion.execute("SELECT Nombre from Clientes where id=?",(id_cliente,))
    fila=cursor.fetchone()
    #Conditional simple jijoju
    if fila != None:
        print(fila[0])
    else:
        print("EL ID no existe")
except:
    print("ups")
conexion.close()