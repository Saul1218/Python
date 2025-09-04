#Ejercicio 6
#Contar cuántos registros hay en un archivo CSV.

import pandas as pd

df=pd.read_csv("archivos/datos.csv")

print("cantidad de registros = ",len(df))

print("columnas= ",df.shape[1])
print("filas= ",df.shape[0])