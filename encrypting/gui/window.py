from __future__ import unicode_literals

import sys
from encrypting.logic.rsa import Rsa
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QFileDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from encrypting.config import config
import ntpath
from datetime import date
from .encryption import EncryptionDialog
from .decryption import DecryptionDialog
from .keys_generation import AsymmetricKeyGenerationDialog

class Window(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # with open('encrypting/gui/style.css') as styles:
            # self.setStyleSheet(styles.read())
        self.setWindowTitle(config['gui']['title']) 
        # self.setFixedSize(
            # config['gui']['width'],
            # config['gui']['height']
        # )

        vbox = QVBoxLayout()
        vbox.addWidget(AsymmetricKeyGenerationDialog())

        hbox = QHBoxLayout()
        hbox.addWidget(EncryptionDialog())
        hbox.addWidget(DecryptionDialog())
        vbox.addLayout(hbox)
        central = QWidget()
        central.setLayout(vbox)
        self.setCentralWidget(central)


