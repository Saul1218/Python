#Ejercicio 5
#Ordenar un CSV por la columna "Edad" de menor a mayor.
import pandas as pd

df=pd.read_csv("archivos/datos.csv")


print(df.sort_values(by="edad")["edad"])

