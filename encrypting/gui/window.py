from __future__ import unicode_literals

import sys
from encrypting.logic.rsa import Rsa
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QFileDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from encrypting.config import config
import ntpath
from datetime import date
from .key_generation import GuiKeyGeneration
from .encryption import GuiEncryption
from .decryption import GuiDecryption

         
class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Window(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # with open('style.css') as styles:
        #     self.setStyleSheet(styles.read())
        self.setWindowTitle(config['gui']['title']) 
        self.setFixedSize(
            config['gui']['width'],
            config['gui']['height']
        )

        vbox = QVBoxLayout()
        vbox.addWidget(GuiKeyGeneration())

        hbox = QHBoxLayout()
        hbox.addWidget(GuiEncryption())
        hbox.addWidget(GuiDecryption())
        vbox.addLayout(hbox)
        central = QWidget()
        central.setLayout(vbox)
        self.setCentralWidget(central)


