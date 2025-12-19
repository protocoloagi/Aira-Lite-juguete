# Aira Lite Juguete

Aira Lite Juguete es un asistente de voz completamente local diseñado para funcionar sin nube.  
Incluye reconocimiento de voz, síntesis de voz, modelo de IA local y módulos de memoria, todo en tu dispositivo.

## Características

- Motor de IA local (Mistral 7B vía Ollama).
- STT local (Whisper).
- TTS local (Piper).
- Memoria a corto y largo plazo (archivos JSON).
- Conversación natural con simulación emocional básica.
- Compatible con Home Assistant (opcional).
- Integración con Aira Madre para sincronización LAN (opcional).
- Ocho idiomas disponibles.

## Instalación

Ejecuta:

python3 instalador.py


El instalador permite configurar:

- Integración con Aira Madre.
- Idioma principal.
- Instalación de motor IA.
- Activación de escucha continua.
- Integración con Home Assistant.
- Instalación de modelos de voz locales.

## Uso

Iniciar el asistente:

aira_juguete
modulos/
emociones.py
percepcion.py
conversacion.py
reglas.py
memoria_corto_plazo.py
memoria_largo_plazo.py
voz.py

memoria/
corto_plazo.json
largo_plazo.json
estado_emocional.json
perfil_usuario.json

voz/
config_voz.json
modelos_piper/
ar.onnx
de.onnx
en.onnx
es.onnx
fr.onnx
hi.onnx
pt.onnx
zh.onnx

dataset/
emociones_basicas.jsonl
frases_estilo.jsonl

scripts/
setup_llm.sh
instalar_voces.sh


## Requisitos

- Python 3.10+
- ffmpeg
- Ollama
- Piper

## Licencia

PALL-0 (libre, sin privatización).
