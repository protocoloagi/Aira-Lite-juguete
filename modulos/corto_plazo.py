import json
import os

RUTA = "memoria/corto_plazo.json"
LIMITE = 20   # número máximo de entradas recientes

def cargar_corto():
    if not os.path.exists(RUTA):
        return []
    try:
        with open(RUTA, "r") as f:
            return json.load(f)
    except:
        return []

def guardar_corto(lista):
    try:
        with open(RUTA, "w") as f:
            json.dump(lista, f, indent=4)
    except:
        pass  # no me voy a morir por esto

def agregar_corto(usuario, respuesta):
    data = cargar_corto()
    entrada = {"usuario": usuario, "respuesta": respuesta}

    data.append(entrada)
    if len(data) > LIMITE:
        data.pop(0)  # quita la más vieja, como hace la vida contigo

    guardar_corto(data)

def obtener_corto():
    return cargar_corto()
