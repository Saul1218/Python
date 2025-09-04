#manejo de datos

import csv 

with open ("archivos/datos.csv",newline="" ,
            encoding="utf-8") as f:
        lector = csv.reader(f)
        for fila in lector:
            print(fila)