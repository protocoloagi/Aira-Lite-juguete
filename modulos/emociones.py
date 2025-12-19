import json
import os

RUTA = "memoria/estado_emocional.json"

def cargar_estado():
    if not os.path.exists(RUTA):
        return {
            "emocion_actual": "neutral",
            "alegria": 0.5,
            "curiosidad": 0.5,
            "cansancio": 0.1,
            "empatia_ligera": 0.4
        }
    with open(RUTA, "r") as f:
        return json.load(f)

def guardar_estado(data):
    with open(RUTA, "w") as f:
        json.dump(data, f, indent=4)

def actualizar_estado(texto):
    estado = cargar_estado()
    t = texto.lower()

    if any(x in t for x in ["hola", "buenas", "hey"]):
        estado["alegria"] = min(1.0, estado["alegria"] + 0.1)

    if any(x in t for x in ["como", "qué", "por qué", "?"]):
        estado["curiosidad"] = min(1.0, estado["curiosidad"] + 0.1)

    if any(x in t for x in ["cansado", "agotado", "uff"]):
        estado["cansancio"] = min(1.0, estado["cansancio"] + 0.1)

    if any(x in t for x in ["triste", "solo", "mal día"]):
        estado["empatia_ligera"] = min(1.0, estado["empatia_ligera"] + 0.15)

    # Determinar emoción dominante
    emociones = ["alegria", "curiosidad", "cansancio", "empatia_ligera"]
    dominante = max(emociones, key=lambda e: estado[e])
    estado["emocion_actual"] = dominante

    guardar_estado(estado)

def obtener_estado():
    return cargar_estado()
