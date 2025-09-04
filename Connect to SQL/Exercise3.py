#: Escribir un nuevo script que se conecte a la base de datos mi_base_de_datos.db, seleccione todos los registros de la tabla clientes y los
#imprima en la consola

import sqlite3

conexion=sqlite3.connect("bd1.db")
cursor=conexion.execute("SELECT id , Nombre from Clientes")
for fila in cursor :
    print(fila)
conexion.close()