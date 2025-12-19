def filtrar(texto):
    """
    Reglas mínimas de higiene verbal.
    """
    t = texto.lower()

    prohibidas = ["mátate", "suicídate", "odio", "racista", "terrorista"]
    for p in prohibidas:
        if p in t:
            return "Prefiero no hablar de eso. Cambiemos de tema."

    if len(t) > 300:
        return t[:300] + "..."

    return texto
