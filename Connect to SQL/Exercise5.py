#: Crear un script que le pida al usuario un ID y un nuevo nombre. 
#El script debe actualizar el registro con el ID proporcionado con el nuevo
#nombre. Confirma la actualización imprimiendo un mensaje.

import sqlite3

#Connecto to database 
conexion=sqlite3.connect("bd1.db")
id_cliente= int(input("Ingrese un ID de Cliente: "))
new_name = input ("Write the new name for the user : ")

try:
    cursor=conexion.execute("UPDATE Clientes SET Nombre=? WHERE id=? ", (new_name,id_cliente))

    if cursor.rowcount>0:
        print("Se actualizo correctamente")
    else:
            print("sos un bolduo")
    conexion.commit()

except:
    print("error")
conexion.close()
