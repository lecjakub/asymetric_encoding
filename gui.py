from __future__ import unicode_literals

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from config import config
import ntpath

def path_leaf(path : str):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

class KeyGeneration(QWidget):
    def __init__(self, *args, **kwargs):
        super(KeyGeneration, self).__init__(*args, **kwargs)
        self.setStyleSheet("background-color: gray; margin:2px;")
        self.asymmetric_algorithms : QComboBox = None
        vbox = QVBoxLayout()
        title = QLabel("Asymmetric Key Generation")
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)

        generation_bar = QHBoxLayout()
        generation_bar.addWidget(QLabel("Choose asymmetric algorithm"))
        self.asymmetric_algorithms = QComboBox()
        self.asymmetric_algorithms.addItems(config['algorithms']['asymmetric'])
        generation_bar.addWidget(self.asymmetric_algorithms)

        generate_key_button = QPushButton("Generate keys")
        generate_key_button.clicked.connect(self.generate_keys)
        generation_bar.addWidget(generate_key_button)
        vbox.addLayout(generation_bar)
        self.setLayout(vbox)

    def generate_keys(self):
        print("generating keys for %s" % self.asymmetric_algorithms.currentText())

class Encryption(QWidget):
    def __init__(self, *args, **kwargs):
        super(Encryption, self).__init__(*args ,**kwargs)
        self.symmetric_combobox :QComboBox = None
        self.public_key_path:str = None
        self.public_key_label :QLabel = None


        self.setStyleSheet("background-color: cadetblue; margin: 2px;")
        vbox = QVBoxLayout()
        title = QLabel("Encrypting")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("padding: 2em;")
        vbox.addWidget(title)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Choose symmetric algorithm:"))
        self.symmetric_combobox = QComboBox();
        self.symmetric_combobox.addItems(config['algorithms']['symmetric'])
        hbox.addWidget(self.symmetric_combobox)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        self.public_key_label = QLabel('Public key file')
        hbox.addWidget(self.public_key_label)
        loading_files_button = QPushButton("Load public key")
        loading_files_button.clicked.connect(self.load_public_key)
        hbox.addWidget(loading_files_button)
        vbox.addLayout(hbox)
        



        self.setLayout(vbox)

    def load_public_key(self):
        pass

class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Gui(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Gui, self).__init__(*args, **kwargs)
        with open('style.css') as styles:
            self.setStyleSheet(styles.read())
        self.setWindowTitle(config['gui']['title']) 
        self.setFixedSize(
            config['gui']['width'],
            config['gui']['height']
        )

        vbox = QVBoxLayout()
        vbox.addWidget(KeyGeneration())

        hbox = QHBoxLayout()
        hbox.addWidget(Encryption())
        hbox.addWidget(Color('green'))
        vbox.addLayout(hbox)
        central = QWidget()
        central.setLayout(vbox)
        self.setCentralWidget(central)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Gui()
    window.show()
    sys.exit(app.exec_())
