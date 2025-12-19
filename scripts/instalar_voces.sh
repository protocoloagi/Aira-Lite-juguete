#!/bin/bash

mkdir -p voz/modelos_piper

echo "Descargando modelos de voz..."

wget -O voz/modelos_piper/ar.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/ar/arabic_Modares/medium/arabic_Modares_medium.onnx"

wget -O voz/modelos_piper/de.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/de/thorsten/medium/de_thorsten_medium.onnx"

wget -O voz/modelos_piper/en.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US_amy_medium.onnx"

wget -O voz/modelos_piper/es.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_ES/sharvard/medium/es_ES-sharvard-medium.onnx"

wget -O voz/modelos_piper/fr.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/siwis/medium/fr_FR_siwis_medium.onnx"

wget -O voz/modelos_piper/hi.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/hi/hi_IN/cmu_awb/medium/hi_IN_cmu-awb-medium.onnx"

wget -O voz/modelos_piper/pt.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/br/edresson/medium/pt_br_edresson_medium.onnx"

wget -O voz/modelos_piper/zh.onnx \
"https://huggingface.co/rhasspy/piper-voices/resolve/main/zh/zh_CN/cn/medium/zh_CN-cn-medium.onnx"

echo "Modelos de voz descargados correctamente."
