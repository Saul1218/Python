import requests
import json
import csv

# 1. Consumir la API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Error al consumir la API")
    data = []

# Guardar toda la información en un archivo JSON
with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

usuarios = []
for i in range(1, 6):  # Ejemplo: primeros 5 usuarios
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{i}")
    if response.status_code == 200:
        usuarios.append(response.json())

# Guardamos en otro JSON
with open("usuarios_id.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)

# Crear un CSV con campos seleccionados
with open("usuarios.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nombre", "email", "ciudad"])  # encabezados
    
    for u in data:
        writer.writerow([u["id"], u["name"], u["email"], u["address"]["city"]])
