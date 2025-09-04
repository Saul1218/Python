#Ejercicio 4
#Filtrar de un CSV a todas las personas mayores de 30 años.

import pandas as pd
df=pd.read_csv("archivos/datos.csv")

filtro=df[df["edad"]>30]
print(filtro)