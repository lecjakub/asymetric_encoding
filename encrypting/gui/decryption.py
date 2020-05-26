from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
import encrypting.gui.dialogs as dialogs

class GuiDecryption(QWidget):
    def __init__(self, *args, **kwargs):
        super(GuiDecryption, self).__init__(*args, **kwargs)
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
            filename = dialogs.path_leaf(self.private_key_path)
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

