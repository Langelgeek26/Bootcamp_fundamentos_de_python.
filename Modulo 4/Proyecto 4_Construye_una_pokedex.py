import requests      # Esta librería permite hacer peticiones HTTP a la API.
import os
import json
from io import BytesIO        # Esta clase permite manejar imágenes como objetos en memoria.
from PIL import Image, ImageTk
import tkinter as tk

def traducir_nombre(url, idioma="es"):
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        return None
    datos = respuesta.json()
    for nombre in datos.get("names", []):
        if nombre["language"]["name"] == idioma:
            return nombre["name"]
    return datos.get("name", "Desconocido")

# Esta función recoge toda la información importante del Pokémon.
def datos_del_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        print(f"Error: El Pokémon '{nombre}' no fue encontrado.")
        return None

    datos = respuesta.json()

    tipos = []
    for t in datos["types"]:
        tipo_url = t["type"]["url"]
        nombre_tipo = traducir_nombre(tipo_url)
        if nombre_tipo:
            tipos.append(nombre_tipo)

    habilidades = []
    for h in datos["abilities"]:
        habilidad_url = h["ability"]["url"]
        nombre_habilidad = traducir_nombre(habilidad_url)
        if nombre_habilidad:
            habilidades.append(nombre_habilidad)

    movimientos = []
    for m in datos["moves"][:5]:
        movimiento_url = m["move"]["url"]
        nombre_movimiento = traducir_nombre(movimiento_url)
        if nombre_movimiento:
            movimientos.append(nombre_movimiento)

    # Se devuelve todo junto en forma de diccionario.
    return {
        "nombre": datos["name"].capitalize(),        
        "peso_kg": datos["weight"] / 10,             
        "altura_m": datos["height"] / 10,            
        "imagen": datos["sprites"]["front_default"], 
        "tipo": tipos,
        "habilidades": habilidades,
        "movimientos": movimientos
    }

def mostrar_info(info):
    print("\nInformación del Pokémon:")
    print(f"Imagen: {info['imagen']}")
    print(f"Altura: {info['altura_m']} m")
    print(f"Peso: {info['peso_kg']} kg")
    print(f"Tipo: {', '.join(info['tipo'])}")
    print(f"Habilidades: {', '.join(info['habilidades'])}")
    print(f"Movimientos: {', '.join(info['movimientos'])}")

def mostrar_imagen(url_imagen):
    respuesta = requests.get(url_imagen)
    if respuesta.status_code != 200:
        print("No se pudo cargar la imagen.")
        return

    imagen_bytes = BytesIO(respuesta.content)
    imagen_pil = Image.open(imagen_bytes)

    ventana = tk.Tk()
    ventana.title("Pokémon")

    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    etiqueta = tk.Label(ventana, image=imagen_tk)
    etiqueta.pack()

    ventana.mainloop()

# Esta función guarda todos los datos del Pokémon en un archivo .json dentro de una carpeta "pokedex".
def guardar_en_json(info):
    os.makedirs("pokedex", exist_ok=True)  # Crea la carpeta si no existe.
    ruta = f"pokedex/{info['nombre']}.json"
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(info, archivo, indent=4, ensure_ascii=False)
    print(f"Información guardada en '{ruta}'")

def main():
    nombre = input("Introduce el nombre de un Pokémon: ").strip()
    if not nombre:
        print("Debes escribir un nombre.")
        return

    info = datos_del_pokemon(nombre)
    if info:
        mostrar_info(info)
        mostrar_imagen(info["imagen"])
        guardar = input("¿Deseas guardar esta información? (s/n): ").strip().lower()
        if guardar == 's':
            guardar_en_json(info)
        else:
            print("No se guardó el archivo.")

if __name__ == "__main__":
    main()