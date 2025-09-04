import json

with open("archivos/jugadores.json" ,"r",encoding ="utf-8" )as f:
    data=json.load(f)

    print(data["jugadores"][1]["edad"])