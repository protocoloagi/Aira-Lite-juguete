import json
import random

from modulos.memoria_corto_plazo import obtener_corto
from modulos.memoria_largo_plazo import obtener_largo

RUTA_FRASES = "dataset/frases_estilo.jsonl"

def cargar_frases():
    frases = []
    with open(RUTA_FRASES, "r") as f:
        for linea in f:
            try:
                frases.append(json.loads(linea))
            except:
                pass
    return frases

FRASES = cargar_frases()

def seleccionar_estilo(emocion):
    if emocion == "alegria":
        return "alegre"
    if emocion == "curiosidad":
        return "curioso"
    if emocion == "cansancio":
        return "neutral"
    if emocion == "empatia_ligera":
        return "suave"
    return "neutral"

def frase_estilo(estilo):
    opciones = [f["frase"] for f in FRASES if f["estilo"] == estilo]
    if not opciones:
        opciones = ["Ok, te sigo."]
    return random.choice(opciones)

def generar_respuesta(texto, emocion, memoria):
    estilo = seleccionar_estilo(emocion["emocion_actual"])
    frase_base = frase_estilo(estilo)

    memoria_texto = ""
    largo = obtener_largo()
    if largo["gustos"]:
        memoria_texto += f"El usuario tiene gustos: {', '.join(largo['gustos'])}. "
    if largo["frases_recurrentes"]:
        memoria_texto += f"Suele repetir: {', '.join(largo['frases_recurrentes'])}. "

    prompt = f"""
Eres Aira Lite Juguete, hablas de forma ligera, natural y amable.
Estilo base: {estilo}.
Contexto emocional: {emocion['emocion_actual']}.

Frase estilo sugerida: "{frase_base}"

Memoria relevante: {memoria_texto}

Usuario dijo: "{texto}"

Responde de forma breve, natural y humana.
"""

    return prompt.strip()
