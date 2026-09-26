from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QLineEdit,
                            QPushButton, QVBoxLayout, QHBoxLayout)
from config import *


class TestWindow(QWidget):
    def __init__(self, title=TXT_TITLE):
        self.title = title
        super().__init__()
        self.set_ui()
        self.config_window()
        self.show()

    def set_ui(self):
        # ESTABLECER WIDGETS
        self.welcome_label = QLabel('SEGUNDA VENTANA')

        # LAYOUT
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.welcome_label, alignment=Qt.AlignLeft)


        self.setLayout(self.main_layout)

    def config_window(self):
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)
        self.setStyleSheet(STYLES)


