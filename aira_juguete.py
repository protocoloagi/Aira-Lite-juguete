import json
import subprocess
import time
import os
import sys

from modulos.emociones import actualizar_estado_emocional
from modulos.percepcion import analizar_entrada
from modulos.conversacion import generar_respuesta
from modulos.corto_plazo import guardar_memoria_corto_plazo
from modulos.largo_plazo import guardar_memoria_largo_plazo
from modulos.reglas import permitir_respuesta
from modulos.voz import hablar

# Nuevo módulo Aira Madre
from modulos.aira_madre import enviar_estado, solicitar_actualizaciones


CONFIG_PATH = "config.json"
MEMORIA_CP = "memoria/corto_plazo.json"
MEMORIA_LP = "memoria/largo_plazo.json"
EMOCIONES = "memoria/estado_emocional.json"


def cargar_config():
    if not os.path.exists(CONFIG_PATH):
        print("No existe config.json. Ejecute el instalador.")
        sys.exit(1)
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def cargar_memoria(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        try:
            return json.load(f)
        except:
            return {}


def guardar_memoria(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def escuchar_whisper():
    """ Captura audio y lo envía a Whisper local vía Ollama. """
    print("[Aira] Escuchando...")

    subprocess.run(["ffmpeg", "-y", "-f", "pulse", "-i", "default",
                    "-t", "3", "input.wav"],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

    resultado = subprocess.run(
        ["ollama", "run", "whisper", "<", "input.wav"],
        capture_output=True,
        text=True,
        shell=True
    )

    return resultado.stdout.strip()


def aplicar_actualizaciones(actualizaciones, memoria_largo, config):
    """Aplica las actualizaciones enviadas por Aira Madre."""

    if not actualizaciones:
        return memoria_largo, config

    # Reglas nuevas
    if "nuevas_reglas" in actualizaciones:
        memoria_largo["reglas_dinamicas"] = actualizaciones["nuevas_reglas"]

    # Estilo conversacional
    if "estilo" in actualizaciones:
        memoria_largo["estilo_conversacion"] = actualizaciones["estilo"]

    # Cambios en parámetros de voz
    if "voz" in actualizaciones:
        try:
            with open("voz/config_voz.json", "r") as f:
                cfg_voz = json.load(f)

            cfg_voz.update(actualizaciones["voz"])

            with open("voz/config_voz.json", "w") as f:
                json.dump(cfg_voz, f, indent=4)

        except:
            print("[Aira] No se pudo actualizar la voz desde AM.")

    return memoria_largo, config


def main_loop():
    config = cargar_config()
    idioma = config["idioma"]

    memoria_corto = cargar_memoria(MEMORIA_CP)
    memoria_largo = cargar_memoria(MEMORIA_LP)
    estado_emocional = cargar_memoria(EMOCIONES)

    print(">>> Aira Lite Juguete iniciada.")
    print(">>> Integración con Aira Madre: ACTIVADA" if config["integracion_am"] else ">>> Sin integración AM.")
    print(">>> Presione CTRL+C para salir.\n")

    while True:
        try:
            entrada_usuario = escuchar_whisper()

            if not entrada_usuario:
                continue

            print(f"[Usuario] {entrada_usuario}")

            if not analizar_entrada(entrada_usuario):
                continue

            if not permitir_respuesta(entrada_usuario):
                print("[Aira] (Respuesta bloqueada por reglas)")
                continue

            estado_emocional = actualizar_estado_emocional(
                entrada_usuario, estado_emocional
            )
            guardar_memoria(EMOCIONES, estado_emocional)

            # IA local con memoria
            respuesta = generar_respuesta(
                entrada_usuario,
                memoria_corto,
                memoria_largo
            )

            print(f"[Aira] {respuesta}")

            # Guardar memorias
            guardar_memoria_corto_plazo(memoria_corto, entrada_usuario, respuesta)
            guardar_memoria(MEMORIA_CP, memoria_corto)

            memoria_largo = guardar_memoria_largo_plazo(
                memoria_largo, entrada_usuario, respuesta
            )
            guardar_memoria(MEMORIA_LP, memoria_largo)

            # HABLAR
            hablar(respuesta, idioma=idioma)

            # -------- INTEGRACIÓN AIRA MADRE COMPLETA --------
            if config["integracion_am"]:
                # Enviar estado
                enviar_estado(memoria_largo, estado_emocional)

                # Recibir actualizaciones
                actualizaciones = solicitar_actualizaciones()

                # Aplicarlas
                memoria_largo, config = aplicar_actualizaciones(
                    actualizaciones, memoria_largo, config
                )
            # --------------------------------------------------

            time.sleep(0.3)

        except KeyboardInterrupt:
            print("\nCerrando...")
            sys.exit(0)


if __name__ == "__main__":
    main_loop()
