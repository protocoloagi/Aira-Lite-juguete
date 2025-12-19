def analizar_input(texto):
    """
    Decide si el mensaje merece respuesta.
    Evita ruido, mensajes vacíos o sonidos.
    """
    if not texto:
        return False
    
    t = texto.strip().lower()

    if len(t) < 2:
        return False

    if t in ["mmm", "eh", "ah", "oh"]:
        return False

    # Palabras que fuerzan respuesta
    triggers = ["oye", "aira", "dime", "cuéntame", "qué", "como", "por qué"]
    if any(x in t for x in triggers):
        return True

    # Si parece frase normal, responde
    if " " in t:
        return True

    return False
