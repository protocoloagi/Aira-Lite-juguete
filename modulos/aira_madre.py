import json
import os
import requests
import time


CONEXION_RUTA = "conexion_am.json"


def cargar_conexion():
    if not os.path.exists(CONEXION_RUTA):
        return None
    
    with open(CONEXION_RUTA, "r") as f:
        return json.load(f)


def enviar_estado(memoria_largo, emociones):
    """
    Envía a Aira Madre el estado actual de la instancia Juguete.
    """
    cfg = cargar_conexion()
    if not cfg:
        return None

    try:
        respuesta = requests.post(
            cfg["endpoint"] + "/sync_estado",
            json={
                "token": cfg["token"],
                "memoria_largo": memoria_largo,
                "emociones": emociones,
            },
            timeout=2
        )
        return respuesta.json()
    except:
        return None


def solicitar_actualizaciones():
    """
    Pide a Aira Madre las reglas nuevas, estilo, ajustes de voz, etc.
    """
    cfg = cargar_conexion()
    if not cfg:
        return None

    try:
        r = requests.post(
            cfg["endpoint"] + "/sync_pedir",
            json={ "token": cfg["token"] },
            timeout=2
        )
        return r.json()
    except:
        return None
