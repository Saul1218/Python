#EJERCICIO 8
#LEER UN JSON Y ACCEDER AL VALOR DE UNA CLAVE ESPECIFICA

import json 

with open("archivos/jugadores.json","r",encoding="utf-8") as f:
    data=json.load()

