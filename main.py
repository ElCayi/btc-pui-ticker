"""
Módulo principal para la aplicación PuiTicker.

Este módulo contiene la clase principal :class:`PuiTicker` que implementa un widget
de escritorio flotante para mostrar el precio de futuros de BTC/USDC en tiempo real
utilizando la API de Binance.
"""
import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap

def resource_path(relative_path):
    """ Obtiene la ruta absoluta al recurso, funciona para dev y para PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class PuiTicker(QWidget):
    """
    Widget flotante que muestra el precio de BTC/USDC.

    Esta clase hereda de :class:`QWidget` y crea una ventana sin bordes,
    siempre visible (always-on-top), con una imagen de fondo y una etiqueta
    que se actualiza periódicamente con el precio actual.
    """

    def __init__(self):
        """
        Inicializa el widget PuiTicker.

        Configura la ventana, carga la imagen de fondo, configura las etiquetas
        y botones, e inicia el temporizador para la actualización del precio.
        """
        super().__init__()

        # Variables para arrastrar la ventana
        self._startPos = None

        # Configurar ventana sin borde y siempre al frente
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Imagen del monstruito
        self.imagen_label = QLabel(self)
        self.pixmap = QPixmap(resource_path("btc-pui.png"))  # Usa tu PNG aquí (tu monstruito)
        self.imagen_label.setPixmap(self.pixmap)
        self.imagen_label.resize(self.pixmap.width(), self.pixmap.height())

        # Label para el precio → en el óvalo blanco
        self.label = QLabel("Cargando precio...", self)
        self.label.setFont(QFont("Arial", 20, QFont.Bold))
        self.label.setStyleSheet("color: black;")  # Negro para que quede bien en el óvalo blanco
        self.label.setAlignment(Qt.AlignCenter)

        # Coloca el label en el óvalo blanco (ajusta estos valores a tu imagen)
        self.label_width = 240
        self.label_height = 80
        self.label_x = (self.pixmap.width() - self.label_width) // 2
        self.label_y = (self.pixmap.height() // 2) - 20  # Ajusta según el diseño

        self.label.resize(self.label_width, self.label_height)
        self.label.move(self.label_x, self.label_y)

        # Botón para cerrar ventana
        self.close_button = QPushButton("❌", self)
        self.close_button.setFont(QFont("Arial", 14))
        self.close_button.setStyleSheet("background-color: rgba(0,0,0,100); color: white; border-radius: 10px;")
        self.close_button.resize(40, 40)
        self.close_button.move(10, 10)
        self.close_button.clicked.connect(QApplication.instance().quit)

        # Timer para actualizar el precio cada 2 segundos
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_precio)
        self.timer.start(2000)

        # Primera actualización
        self.actualizar_precio()

        # Ajustar ventana al tamaño de la imagen
        self.resize(self.pixmap.width(), self.pixmap.height())

    def obtener_precio_futuros_btc(self):
        """
        Obtiene el precio actual de futuros de BTC/USDC desde Binance.

        Realiza una petición HTTP GET a la API de futuros de Binance.

        :return: El precio actual de BTC en USDC o None si ocurre un error.
        :rtype: float or None
        """
        try:
            url = "https://fapi.binance.com/fapi/v1/ticker/price?symbol=BTCUSDC"
            respuesta = requests.get(url, timeout=5)
            datos = respuesta.json()
            precio = float(datos["price"])
            return precio
        except Exception as e:
            print(f"Error al obtener precio: {e}")
            return None

    def actualizar_precio(self):
        """
        Actualiza la etiqueta de precio en la interfaz.

        Llama a :meth:`obtener_precio_futuros_btc` y actualiza el texto del label.
        Si hay un error, muestra "Error".
        """
        precio = self.obtener_precio_futuros_btc()
        if precio is not None:
            self.label.setText(f'<span style="font-size: 40px;">{precio:.2f}</span> <span style="font-size: 20px;">USDC</span>')
        else:
            self.label.setText("Error")

    # Métodos para arrastrar la ventana
    def mousePressEvent(self, event):
        """
        Maneja el evento de presionar el botón del mouse.

        Registra la posición inicial para permitir el arrastre de la ventana.

        :param event: El evento del mouse.
        :type event: QMouseEvent
        """
        if event.button() == Qt.LeftButton:
            self._startPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        """
        Maneja el evento de mover el mouse.

        Mueve la ventana si el botón izquierdo está presionado.

        :param event: El evento del mouse.
        :type event: QMouseEvent
        """
        if event.buttons() == Qt.LeftButton and self._startPos is not None:
            self.move(event.globalPos() - self._startPos)
            event.accept()

    def mouseReleaseEvent(self, event):
        """
        Maneja el evento de soltar el botón del mouse.

        Finaliza la operación de arrastre.

        :param event: El evento del mouse.
        :type event: QMouseEvent
        """
        self._startPos = None
        event.accept()

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PuiTicker()
    ventana.show()
    sys.exit(app.exec_())

