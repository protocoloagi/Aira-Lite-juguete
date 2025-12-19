import json
import os
from collections import Counter

RUTA = "memoria/largo_plazo.json"

def cargar_largo():
    if not os.path.exists(RUTA):
        return {"gustos": [], "frases_recurrentes": []}
    try:
        with open(RUTA, "r") as f:
            return json.load(f)
    except:
        return {"gustos": [], "frases_recurrentes": []}

def guardar_largo(data):
    with open(RUTA, "w") as f:
        json.dump(data, f, indent=4)

def consolidar_memoria(corto):
    """
    Mira el corto plazo y detecta repeticiones tontas:
    - gustos del usuario ("me gusta X")
    - frases frecuentes
    """

    largo = cargar_largo()

    frases = [x["usuario"].lower() for x in corto]

    # detectar gustos
    for f in frases:
        if "me gusta" in f:
            gusto = f.split("me gusta")[-1].strip()
            if gusto and gusto not in largo["gustos"]:
                largo["gustos"].append(gusto)

    # detectar frases recurrentes
    contador = Counter(frases)
    recurrentes = [f for f, c in contador.items() if c >= 3]

    for r in recurrentes:
        if r not in largo["frases_recurrentes"]:
            largo["frases_recurrentes"].append(r)

    guardar_largo(largo)

def obtener_largo():
    return cargar_largo()
