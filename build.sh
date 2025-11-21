#!/bin/bash

APP_NAME="btc-pui-ticker"

echo "🚀 Iniciando compilación de $APP_NAME para Linux..."

# 1. Limpiar compilaciones previas para evitar errores de caché
rm -rf build/ dist/ *.spec

# 2. Ejecutar PyInstaller
# --clean: Limpia caché de PyInstaller
# --noconsole: No muestra terminal al ejecutar
# --onefile: Un solo ejecutable
# --collect-all PyQt5: VITAL para que incluya todas las librerías gráficas dentro
# --add-data "btc-pui.png:.": Incluye la imagen en el ejecutable (formato origen:destino)
pyinstaller --noconsole --onefile --clean --name="$APP_NAME" --collect-all PyQt5 --add-data "btc-pui.png:." main.py

echo "✅ Compilación terminada."
echo "📂 El ejecutable está en: dist/$APP_NAME"
echo "👉 Para probarlo ejecuta: ./dist/$APP_NAME"