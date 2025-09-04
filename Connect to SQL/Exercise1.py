# Escribir un script de Python que se conecte a una base de datos SQLite. Si el archivo de la base de datos no existe, se creará
# automáticamente. Luego, el script debe crear una tabla llamada clientes con las columnas id (entero, clave primaria) y nombre(texto).
import sqlite3
conexion=sqlite3.connect("bd1.db")
#Bloque de excepcion o control de manejo de errores
try: 
    conexion.execute("""create table Clientes (id integer primary key autoincrement , Nombre text ) """ )
    print("Se creo la tabla Clientes")
except:
    print("la tabla Clientes ya existe")
conexion.close

