import requests
import csv

def get_json(URL: str):
    resp = requests.get(URL)
    resp.raise_for_status()
    return resp.json()

def get_digimon_data():
    data = get_json("https://digi-api.com/api/v1/digimon/")

    digimons_list = []
    
    for digimon in data['content'][:10]:  
        name = digimon['name']
        image_url = digimon['image']
        digimons_list.append({"name": name, "image_url": image_url})
    
    return digimons_list

def download_image(image_url: str, filename: str):
    resp = requests.get(image_url)
    resp.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(resp.content)
    print(f"Imagen de {filename} guardada.")

def show_digimons(digimons_list):
    for digimon in digimons_list:
        print(f"Nombre: {digimon['name']}")
        print(f"Imagen URL: {digimon['image_url']}")

        download_image(digimon['image_url'], f"{digimon['name']}.png")

def save_to_csv(digimons_list, filename='digimons.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "image_url"])
        writer.writeheader()  
        writer.writerows(digimons_list)  
    print(f"Datos guardados en {filename}")

def main():
    digimons_list = get_digimon_data()
    
    show_digimons(digimons_list)
    
    save_to_csv(digimons_list)

if __name__ == "__main__":
    main()
