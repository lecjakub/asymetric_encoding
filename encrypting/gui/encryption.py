from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from encrypting.config import config
import encrypting.gui.dialogs as dialogs


class GuiEncryption(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
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
            filename = dialogs.file_from_path(self.public_key_path)
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
   