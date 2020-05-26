from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QPushButton, QWidget
from PyQt5.QtCore import Qt
from encrypting.config import config
from encrypting.logic.rsa import Rsa
from .dialogs import get_file_to_save


class GuiKeyGeneration(QWidget):
    def __init__(self, *args, **kwargs):
        super(GuiKeyGeneration, self).__init__(*args, **kwargs)
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

