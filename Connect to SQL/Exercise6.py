#Escribir un script que le pida al usuario un ID de cliente . El script debe eliminar el registro correspondiente a ese
#ID y confirmar que la eliminacion fue exitosa .
import sqlite3

#Connecto to database 
conexion=sqlite3.connect("bd1.db")
id_cliente= int(input("Ingrese un ID de Cliente: "))
try:
    #Delete the register 
    cursor=conexion.execute("DELETE FROM Clientes WHERE id=?" , (id_cliente,))
    conexion.commit()   
    if cursor.rowcount>0:
        print("Se elimino correctamente")
    else:
        print("Ya esta eliminado")
     

except sqlite3.Error as e:
    print("error con la base de datos" ,e)
conexion.close()