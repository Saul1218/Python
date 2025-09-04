#2: Modificar el script del problema 1 para insertar tres registros en la tabla clientes. Cada registro debe tener un nombre de cliente
#diferente.

import sqlite3
conexion=sqlite3.connect("bd1.db")
try: 
   conexion.execute("INSERT INTO Clientes(Nombre)values(?,?)",("Saul"))
   conexion.execute("INSERT INTO Clientes(Nombre)values(?,?)",("Yas"))
   conexion.execute("INSERT INTO Clientes(Nombre)values(?,?)",("Flor"))
   conexion.commit()
except:
    print("La tabla Clientes ya existe")
conexion.close()