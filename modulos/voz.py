import json
import subprocess
import os

CONFIG_RUTA = "voz/config_voz.json"

def cargar_config_voz():
    if not os.path.exists(CONFIG_RUTA):
        raise Exception("Falta config_voz.json en carpeta voz/")
    with open(CONFIG_RUTA, "r") as f:
        return json.load(f)

def hablar(texto, idioma="es"):
    cfg = cargar_config_voz()
    idiomas = cfg["idiomas"]

    if idioma not in idiomas:
        idioma = cfg["por_defecto"]

    modelo = idiomas[idioma]["modelo"]
    velocidad = idiomas[idioma]["velocidad"]

    cmd = [
        "piper",
        "--model", modelo,
        "--output", "respuesta.wav",
        "--text", texto,
        "--length-scale", str(velocidad)
    ]

    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([
            "ffplay", "-nodisp", "-autoexit", "respuesta.wav"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print("Error de voz:", e)
