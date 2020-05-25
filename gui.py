from __future__ import unicode_literals

import sys
from rsa import Rsa
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QFileDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from config import config
import ntpath
from datetime import date
from asymkey import AsymKey
from core import encrypt_files, decrypt_files

def get_directory_to_save(title):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    directory = QFileDialog.getExistingDirectory(None, caption=title, options=options)
    return directory

def get_file_to_save(title):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getSaveFileName(None, caption=title, options=options)
    return filename

def path_leaf(path : str):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

class KeyGeneration(QWidget):
    def __init__(self, *args, **kwargs):
        super(KeyGeneration, self).__init__(*args, **kwargs)
        # self.setStyleSheet("background-color: gray; margin:2px;")
        self.asymmetric_algorithms : QComboBox = None
        vbox = QVBoxLayout()
        title = QLabel("Asymmetric Key Generation")
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)

        # choosing asymmetric algorithm
        generation_bar = QHBoxLayout()
        generation_bar.addWidget(QLabel("Choose asymmetric algorithm"))
        self.asymmetric_algorithms = QComboBox()
        self.asymmetric_algorithms.addItems(config['algorithms']['asymmetric'])
        generation_bar.addWidget(self.asymmetric_algorithms)

        # button for keys generation
        generate_key_button = QPushButton("Generate keys")
        generate_key_button.clicked.connect(self.generate_keys)
        generation_bar.addWidget(generate_key_button)
        vbox.addLayout(generation_bar)
        self.setLayout(vbox)

    def generate_keys(self):
        choosen_asymmetric_algorithm = self.asymmetric_algorithms.currentText()
        if choosen_asymmetric_algorithm == 'rsa1024':
            asym_key = Rsa.generate_key(1024)
        elif choosen_asymmetric_algorithm == 'rsa2048':
            asym_key = Rsa.generate_key(2048)
        else:
            raise TypeError("Unknown algorithm")
        
        save_dir_path = get_file_to_save('Choose file to save key')
        with open(save_dir_path, "wb") as private_key_file:          
            private_key_file.write(asym_key.private_to_bytes())
        with open(save_dir_path + '.pub', "wb") as public_key_file:
            public_key_file.write(asym_key.public_to_bytes())

class Encryption(QWidget):
    def __init__(self, *args, **kwargs):
        super(Encryption, self).__init__(*args ,**kwargs)
        self.symmetric_combobox :QComboBox = None
        self.public_key_path:str = None
        self.public_key_label :QLabel = None
        self.files_to_encrypt = []        


        # self.setStyleSheet("background-color: white; margin: 2px;")
        vbox = QVBoxLayout()
        title = QLabel("Encrypting")
        title.setAlignment(Qt.AlignCenter)
        # title.setStyleSheet("padding: 2em;")
        vbox.addWidget(title)

        # choosing symmetric algorithm
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Choose symmetric algorithm:"))
        self.symmetric_combobox = QComboBox()
        self.symmetric_combobox.addItems(config['algorithms']['symmetric'])
        hbox.addWidget(self.symmetric_combobox)
        vbox.addLayout(hbox)

        # loading public key
        hbox = QHBoxLayout()
        self.public_key_label = QLabel('Public key file')
        hbox.addWidget(self.public_key_label)
        public_key_button = QPushButton("Load public key")
        public_key_button.clicked.connect(self.load_public_key)
        hbox.addWidget(public_key_button)
        vbox.addLayout(hbox)

        # choosing files to encrypt
        files_to_encrypt_button = QPushButton("Choose files")
        files_to_encrypt_button.clicked.connect(self.load_files_to_encrypt)
        vbox.addWidget(files_to_encrypt_button)

        # button for encrypting action
        encrypting_button = QPushButton("Encrypt files")
        encrypting_button.clicked.connect(self.encrypt_files)
        vbox.addWidget(encrypting_button)
        
        self.setLayout(vbox)

    def load_public_key(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.public_key_path, _ = QFileDialog.getOpenFileName(self, "Loading public key")
        if self.public_key_path:
            filename = path_leaf(self.public_key_path)
            self.public_key_label.setText(filename)

    def load_files_to_encrypt(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.files_to_encrypt, _ = QFileDialog.getOpenFileNames(self, "Choose files to encrypt")
        if len(self.files_to_encrypt):
            print("Files to encrypt: ", end='')
            print(self.files_to_encrypt)

    def encrypt_files(self):
        if len(self.files_to_encrypt) and self.public_key_path:
            current_symmetric_algorithm = self.symmetric_combobox.currentText()
            encrypt_files(file_paths=self.files_to_encrypt, public_key_path=self.public_key_path, alg_sym=current_symmetric_algorithm)
        if len(self.files_to_encrypt) == 0:
            print("No files given")
        if self.public_key_path is None:
            print("Public key not given")
            
class Decryption(QWidget):
    def __init__(self, *args, **kwargs):
        super(Decryption, self).__init__(*args, **kwargs)
        self.private_key_path:str = None
        self.private_key_label:QLabel = None
        self.files_to_decrypt = []

        vbox = QVBoxLayout()
        title = QLabel("Decrypting")
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)
        
        # loading private key
        hbox = QHBoxLayout()
        self.private_key_label = QLabel("Private key file")
        hbox.addWidget(self.private_key_label)
        private_key_button = QPushButton("Load private key")
        private_key_button.clicked.connect(self.load_private_key)
        hbox.addWidget(private_key_button)
        vbox.addLayout(hbox)
    
        # choosing files to decrypt
        files_to_decrypt_button = QPushButton("Choose files")
        files_to_decrypt_button.clicked.connect(self.load_files_to_decrypt)
        vbox.addWidget(files_to_decrypt_button)
        
        # button for decrypting action
        decrypting_button = QPushButton("Decrypt files")
        decrypting_button.clicked.connect(self.decrypt_files)
        vbox.addWidget(decrypting_button)


        self.setLayout(vbox)

    def load_private_key(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.private_key_path, _ = QFileDialog.getOpenFileName(self, "Loading public key")
        if self.private_key_path:
            filename = path_leaf(self.private_key_path)
            self.private_key_label.setText(filename)

    def load_files_to_decrypt(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.files_to_decrypt, _ = QFileDialog.getOpenFileNames(self, "Choose files to decrypt")
        if len(self.files_to_decrypt):
            print("Files to decrypt: ", end='')
            print(self.files_to_decrypt)

    def decrypt_files(self):
        if len(self.files_to_decrypt) and self.private_key_path:
            decrypt_files(file_paths=self.files_to_decrypt, private_key_path=self.private_key_path)
        if len(self.files_to_decrypt) == 0:
            print("No files to decrypt given")
        if self.private_key_path is None:
            print("No private key given")

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
        # with open('style.css') as styles:
        #     self.setStyleSheet(styles.read())
        self.setWindowTitle(config['gui']['title']) 
        self.setFixedSize(
            config['gui']['width'],
            config['gui']['height']
        )

        vbox = QVBoxLayout()
        vbox.addWidget(KeyGeneration())

        hbox = QHBoxLayout()
        hbox.addWidget(Encryption())
        hbox.addWidget(Decryption())
        vbox.addLayout(hbox)
        central = QWidget()
        central.setLayout(vbox)
        self.setCentralWidget(central)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = Gui()
    window.show()
    sys.exit(app.exec_())
