from __future__ import unicode_literals

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGridLayout, QHBoxLayout, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from config import config
import ntpath

def path_leaf(path : str):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


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

        # choosing asymmetric algorithm in combobox
        hbox = QHBoxLayout()
        cb_label = QLabel("Choose asymmetric algorithm")
        hbox.addWidget(cb_label)
        self.cb = QComboBox()
        self.cb.addItems(config['algorithms']['asymmetric'])
        # self.cb.currentIndexChanged.connect(self.)
        hbox.addWidget(self.cb)
        self.layout.addLayout(hbox)

        # button signaling generation of files with public and private key
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
        if filename:
            print('saving dummy %s key to %s' %
                  (self.cb.currentText(), filename))
        


class EncryptionModel(Model):
    def __init__(self):
        self.symmetric_cb: QComboBox
        self.public_key_label:QLabel
        self.public_key_path:str
        super().__init__()

    def setup(self):
        self.layout = QVBoxLayout()
        title = QLabel("Encryption")
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)

        # choosing symmetric algorithm from combobox
        hbox = QHBoxLayout()
        symmetric_cb_label = QLabel("Choose symmetric algorithm")
        hbox.addWidget(symmetric_cb_label)
        self.symmetric_cb = QComboBox()
        self.symmetric_cb.addItems(config['algorithms']['symmetric'])
        hbox.addWidget(self.symmetric_cb)
        self.layout.addLayout(hbox)

        # loading public key file
        hbox = QHBoxLayout()
        self.public_key_label = QLabel("Public key file")
        hbox.addWidget(self.public_key_label)
        public_key_button = QPushButton("Load public key")
        public_key_button.clicked.connect(self.load_public_key)
        hbox.addWidget(public_key_button)
        self.layout.addLayout(hbox)         

        # button signaling ecryption action
        hbox = QHBoxLayout()
        encrypt_button = QPushButton('Encrypt file')
        encrypt_button.clicked.connect(self.load_file_to_encrypt)
        hbox.addWidget(encrypt_button)
        self.layout.addLayout(hbox)

    def load_public_key(self):
        options = QFileDialog.Options()
        self.public_key_path, _ = QFileDialog.getOpenFileName(self, "Load public key", options=options)
        if self.public_key_path:
            filename = path_leaf(self.public_key_path)
            self.public_key_label.setText(filename)
            print('public key %s loaded' % self.public_key_path)

    def load_file_to_encrypt(self):
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
        self.private_key_label:QLabel = None
        self.private_key_path:str = None
        super().__init__()

    def setup(self):
        self.layout = QVBoxLayout()
        title = QLabel('Decryption')
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)

        # picking encrypted file
        hbox = QHBoxLayout()
        self.encrypted_file_label = QLabel("Encrypted file")
        hbox.addWidget(self.encrypted_file_label)
        encrypted_button = QPushButton("Pick encrypted file")
        encrypted_button.clicked.connect(self.pick_encrypted_file)
        hbox.addWidget(encrypted_button)
        self.layout.addLayout(hbox)

        # loading private key file
        hbox = QHBoxLayout()
        self.private_key_label = QLabel("Private key file")
        hbox.addWidget(self.private_key_label)
        private_key_button = QPushButton("Load private key")
        private_key_button.clicked.connect(self.load_private_key)
        hbox.addWidget(private_key_button)
        self.layout.addLayout(hbox)         

        # button running decryption
        hbox = QHBoxLayout() 
        decrypting_button = QPushButton("Decrypt file")
        decrypting_button.clicked.connect(self.decryption)
        hbox.addWidget(decrypting_button) 
        self.layout.addLayout(hbox)

    def load_private_key(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Choose file with private key")
        if filename:
            self.private_key_path = path_leaf(filename)
            self.private_key_label.setText(self.private_key_path)

    def pick_encrypted_file(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(
            self, "Choose file you want to decrypt", "", "All Files (*);;Python Files (*.py)", options=options)
        if filename:
            self.encrypted_file_path = path_leaf(filename)
            self.encrypted_file_label.setText(self.encrypted_file_path)

    
    def decryption(self):
        if self.private_key_path and self.encrypted_file_path:
            print("Decrypting %s with key %s" %(self.encrypted_file_path, self.private_key_path))
        if self.private_key_path is None:
            print("Private key not given")
        if self.encrypted_file_path is None:
            print("Encrypted file not given")


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
        with open('style.css') as styles:
            self.setStyleSheet(styles.read())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
