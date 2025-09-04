#Ejercicio 7
# Cargar un archivo CSV y mostrar sus primeras 10 filas

import pandas as pd 

df = pd.read_csv("archivos/datos.csv")

print(df.head(10))