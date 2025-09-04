import pandas as pd

df=pd.read_csv("archivos/datos.csv")

df_ordenado= df.sort_values(by="edad",ascending=True)

print(df_ordenado)