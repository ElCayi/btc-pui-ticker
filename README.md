# BTC Pui Ticker 📈

**BTC Pui Ticker** es un widget de escritorio minimalista y flotante que muestra el precio de **Bitcoin (BTC/USDC)** en tiempo real utilizando la API de Futuros de Binance. Diseñado para traders y entusiastas que desean mantener un ojo en el mercado sin ocupar espacio innecesario en su pantalla.

![BTC Pui Ticker Preview](btc-pui.png)

## ✨ Características

*   **Monitorización en Tiempo Real**: Actualización automática del precio cada 2 segundos.
*   **Siempre Visible**: La ventana se mantiene "Always on Top" (siempre encima de otras ventanas), ideal para trabajar mientras vigilas el precio.
*   **Diseño Flotante**: Interfaz sin bordes (frameless) con fondo transparente y estética personalizada.
*   **Ligero**: Construido con Python y PyQt5, optimizado para un bajo consumo de recursos.
*   **Multiplataforma**: Compatible con Windows, macOS y Linux.

## 🛠️ Requisitos

*   Python 3.11 o superior.
*   Dependencias listadas en `requirements.txt`:
    *   `PyQt5`
    *   `requests`

## 🚀 Entorno de Desarrollo (Dev Container)

Este proyecto está optimizado para **VS Code Dev Containers**. Esto crea un entorno aislado con todas las dependencias y herramientas gráficas preinstaladas, listo para programar.

### Cómo empezar

1.  **Requisitos**: Tener instalado [Docker](https://www.docker.com/) y [VS Code](https://code.visualstudio.com/) con la extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2.  **Abrir**: Abre la carpeta del proyecto en VS Code y selecciona **"Reopen in Container"** cuando se te solicite (o desde la paleta de comandos `F1`).

El contenedor configurará automáticamente Python 3.11, PyQt5 y un entorno de escritorio ligero.

### Ejecutar la aplicación

Dentro de la terminal del contenedor:

```bash
python main.py
```

### Visualizar la GUI

El contenedor incluye un escritorio virtual (Fluxbox) para ver la aplicación gráfica, ya que Docker no tiene pantalla por defecto:
*   **Vía Web (Recomendado)**: Abre `http://localhost:6080` en tu navegador.
*   **Vía VNC**: Conecta tu cliente VNC a `localhost:5901`.

### Compilar el ejecutable (Build)

El proyecto incluye scripts y flujos de trabajo para generar ejecutables independientes (sin necesidad de instalar Python en la máquina destino).

#### Linux / macOS
Puedes usar el script de construcción incluido:
```bash
chmod +x build.sh
./build.sh
```
El ejecutable se generará en la carpeta `dist/`.

#### Windows
Ejecuta el siguiente comando en tu terminal:
```bash
pyinstaller --noconsole --onefile --name="btc-pui-ticker" --collect-all PyQt5 --add-data "btc-pui.png;." main.py
```

## 🤖 Automatización (CI/CD)

Este repositorio cuenta con **GitHub Actions** configurado en `.github/workflows/build.yml` para compilar automáticamente la aplicación para **Windows** y **macOS** cada vez que se hace un push a la rama `main`.

Los artefactos compilados se pueden descargar desde la pestaña "Actions" de GitHub.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo y modificarlo.

---
Desarrollado con ❤️ por [ElCayi](https://github.com/ElCayi)