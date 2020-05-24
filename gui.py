from __future__ import unicode_literals

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGridLayout, QHBoxLayout, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from config import config


class Model(QWidget):
    def __init__(self):
        self.layout = None
        self.setup()
        super().__init__()

    def setup(self):
        raise NotImplemented


class KeyGenModel(Model):
    def __init__(self):
        self.cb: QComboBox = None
        super().__init__()

    def setup(self):
        self.layout = QVBoxLayout()
        title = QLabel("Key generation")
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)

        hbox = QHBoxLayout()
        cb_label = QLabel("Choose asymmetric algorithm")
        hbox.addWidget(cb_label)
        self.cb = QComboBox()
        self.cb.addItems(config['algorithms']['asymmetric'])
        # self.cb.currentIndexChanged.connect(self.)
        hbox.addWidget(self.cb)
        self.layout.addLayout(hbox)

        hbox = QHBoxLayout()
        gen_button = QPushButton("Generate key")
        gen_button.clicked.connect(self.generate_asymmetric_key)
        hbox.addWidget(gen_button)
        self.layout.addLayout(hbox)

    def generate_asymmetric_key(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        # raise NotImplemented
        if filename:
            print('saving dummy %s key to %s' %
                  (self.cb.currentText(), filename))
        


class EncryptionModel(Model):
    def __init__(self):
        self.symmetric_cb: QComboBox
        super().__init__()

    def setup(self):
        self.layout = QVBoxLayout()
        title = QLabel("Encryption")
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)
        hbox = QHBoxLayout()
        symmetric_cb_label = QLabel("Choose symmetric algorithm")
        hbox.addWidget(symmetric_cb_label)
        self.symmetric_cb = QComboBox()
        self.symmetric_cb.addItems(config['algorithms']['symmetric'])
        hbox.addWidget(self.symmetric_cb)
        self.layout.addLayout(hbox)

        # hbox = QHBoxLayout()

        hbox = QHBoxLayout()
        encrypt_button = QPushButton('Encrypt file')
        encrypt_button.clicked.connect(self.encrypt_file)
        hbox.addWidget(encrypt_button)
        self.layout.addLayout(hbox)

    def encrypt_file(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print('encrypting %s' % fileName)


class DecryptionModel(Model):
    def __init__(self):
        self.encrypted_file_label:QLabel = None
        self.encrypted_file_path: str = None
        super().__init__()

    def setup(self):
        self.layout = QVBoxLayout()
        title = QLabel('Decryption')
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)

        hbox = QHBoxLayout()
        self.encrypted_file_label = QLabel("File to decrypt")
        hbox.addWidget(self.encrypted_file_label)
        encrypted_button = QPushButton("Pick encrypted file")
        encrypted_button.clicked.connect(self.pick_file_to_decrypt)
        hbox.addWidget(encrypted_button)
        self.layout.addLayout(hbox)

        hbox = QHBoxLayout()

        # decrypt_button = QPushButton(

    def pick_file_to_decrypt(self):
        pass



class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.title = config['gui']['title']
        self.left = config['gui']['x']
        self.top = config['gui']['y']
        self.width = config['gui']['width']
        self.height = config['gui']['height']
        self.vbox = None
        self.keyGenModel = KeyGenModel()
        self.encryptionModel = EncryptionModel()
        self.decryptionModel = DecryptionModel()
        self.initUI()
        self.layout = None

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        vbox = QVBoxLayout()
        vbox.addLayout(self.keyGenModel.layout)
        vbox.addLayout(self.encryptionModel.layout)
        vbox.addLayout(self.decryptionModel.layout)
        self.setLayout(vbox)
        # with open('style.css') as styles:
        #     self.setStyleSheet(styles.read())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
