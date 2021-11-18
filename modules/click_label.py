from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class Clickedfoto(QLabel):
    """Позволяет отлавливать нажатие мыши на QLabel"""
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()
