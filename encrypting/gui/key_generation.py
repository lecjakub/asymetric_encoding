from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QPushButton, QWidget
from PyQt5.QtCore import Qt
from encrypting.config import config
from encrypting.logic.rsa import Rsa
import encrypting.gui.dialogs as dialogs
from encrypting.logic.algorithms import generate_asymmetric_key


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
        asym_key = generate_asymmetric_key(choosen_asymmetric_algorithm)
        
        save_dir_path = dialogs.save_file('Choose file to save key')
        with open(save_dir_path, "wb") as private_key_file:          
            private_key_file.write(asym_key.private_to_bytes())
        with open(save_dir_path + '.pub', "wb") as public_key_file:
            public_key_file.write(asym_key.public_to_bytes())

