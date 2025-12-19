#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import time

# ------------------------------------------------------------
# UTILIDADES
# ------------------------------------------------------------

def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")


def preguntar(msg):
    return input(f"{msg} (s/n): ").strip().lower()


# ------------------------------------------------------------
# INSTALACIÓN MOTOR IA (OLLAMA + MODELO)
# ------------------------------------------------------------

def instalar_motor_ia():
    print("\n> Instalando motor IA (Ollama + modelo Mistral 7B)...")

    try:
        # Instalar Ollama
        subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh"], stdout=subprocess.DEVNULL)
        subprocess.run(["sh", "install.sh"], stdout=subprocess.DEVNULL)

        # Descargar modelo
        subprocess.run(["ollama", "pull", "mistral"], stdout=subprocess.DEVNULL)

        print("Motor IA instalado.")
        return True
    except Exception as e:
        print(f"ERROR instalando motor IA: {e}")
        return False


# ------------------------------------------------------------
# INSTALACIÓN VOCES (SCRIPT)
# ------------------------------------------------------------

def instalar_voces():
    print("\n> Instalando voces Piper...")
    try:
        subprocess.check_call(["bash", "scripts/instalar_voces.sh"])
        print("Voces instaladas.")
        return True
    except Exception as e:
        print(f"ERROR instalando voces: {e}")
        return False


# ------------------------------------------------------------
# INSTALACIÓN DEPENDENCIAS PYTHON
# ------------------------------------------------------------

def instalar_dependencias_python():
    print("\n> Instalando dependencias Python (requests)...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("Dependencias instaladas.")
        return True
    except Exception as e:
        print(f"ERROR instalando dependencias: {e}")
        return False


# ------------------------------------------------------------
# CONFIGURACIÓN INICIAL (IDIOMA, AIRA MADRE)
# ------------------------------------------------------------

def configurar_sistema():
    print("\n> Configurando parámetros iniciales...")

    idioma = input("Seleccione idioma principal (es/en/fr/de/ar/pt/hi/zh): ").strip().lower()
    if idioma not in ["es","en","fr","de","ar","pt","hi","zh"]:
        idioma = "es"

    integracion = preguntar("¿Desea integrar esta instalación con Aira Madre?")
    integracion_flag = integracion == "s"

    config = {
        "idioma": idioma,
        "integracion_am": integracion_flag
    }

    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

    if integracion_flag:
        token = input("Introduzca token de Aira Madre: ").strip()
        endpoint = input("Introduzca endpoint LAN de Aira Madre (ej: http://192.168.1.50:5555): ").strip()
        
        am = {
            "token": token,
            "endpoint": endpoint
        }

        with open("conexion_am.json", "w") as f:
            json.dump(am, f, indent=4)

    print("Configuración guardada.")
    return config


# ------------------------------------------------------------
# RESUMEN FINAL
# ------------------------------------------------------------

def resumen(motor_ok, voces_ok, dep_ok, config):
    print("\n=====================================")
    print(" INSTALACIÓN COMPLETADA")
    print("=====================================")
    print(f"Motor IA instalado: {'Sí' if motor_ok else 'No'}")
    print(f"Voces instaladas: {'Sí' if voces_ok else 'No'}")
    print(f"Dependencias Python: {'Sí' if dep_ok else 'No'}")
    print(f"Integración con Aira Madre: {'Sí' if config['integracion_am'] else 'No'}")
    print("=====================================")
    print("Para iniciar Aira Lite Juguete ejecute:")
    print("\n    python3 aira_juguete.py\n")
    print("=====================================\n")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

def main():
    limpiar_pantalla()
    print("=====================================")
    print("        INSTALADOR AIRA JUGUETE      ")
    print("=====================================\n")

    motor_ok = False
    voces_ok = False
    dep_ok = False

    instalar_motor = preguntar("¿Desea instalar motor IA (Ollama + Mistral 7B)?")
    instalar_voces_flag = preguntar("¿Desea instalar las voces Piper (8 idiomas)?")
    instalar_dep = preguntar("¿Desea instalar dependencias Python (requests)?")

    if instalar_motor == "s":
        motor_ok = instalar_motor_ia()

    if instalar_voces_flag == "s":
        voces_ok = instalar_voces()

    if instalar_dep == "s":
        dep_ok = instalar_dependencias_python()

    config = configurar_sistema()

    resumen(motor_ok, voces_ok, dep_ok, config)


if __name__ == "__main__":
    main()
