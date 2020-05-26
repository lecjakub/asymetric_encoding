from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHeaderView, QMessageBox, QInputDialog, QLabel, QDialogButtonBox,  QComboBox, QLineEdit, QApplication, QFormLayout, QDialog, QGroupBox
from PyQt5.QtCore import Qt
from encrypting.config import config
from encrypting.gui.helpers import open_file, open_multiple_files, existing_directory
from encrypting.logic.core import encrypt_files


class EncryptionDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.symmetric_algorithm_combobox = QComboBox()
        self.symmetric_algorithm_combobox.addItems(
            config['algorithms']['symmetric'])
        self.public_key = QLineEdit()
        self.public_key.setPlaceholderText('Path to public key file')
        self.files_counter = QLabel("Files loaded: 0")
        self.files = []
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        buttonBox.button(QDialogButtonBox.Ok).setText('Encrypt')
        buttonBox.accepted.connect(self.encrypt)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

    def reject(self):
        """To avoid closing on esc press"""
        pass

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Encryption")
        layout = QFormLayout()
        load_files_button = QPushButton('Load files to encrypt')
        load_files_button.clicked.connect(self.loadFiles)
        layout.addRow(self.files_counter, load_files_button)
        load_public_key_button = QPushButton('Load public key')
        load_public_key_button.clicked.connect(self.loadPublicKey)
        layout.addRow(self.public_key, load_public_key_button)
        layout.addRow(QLabel("Choose symmetric algorithm"),
                      self.symmetric_algorithm_combobox)
        self.formGroupBox.setLayout(layout)

    def loadPublicKey(self):
        filename = open_file('Open public key file')
        if filename is not None:
            self.public_key.setText(filename)

    def loadFiles(self):
        self.files = open_multiple_files('Choose files to encrypt')
        if len(self.files) > 0:
            self.files_counter.setText('Files loaded: %d' % len(self.files))

    def encrypt(self):
        if len(self.public_key.text()) > 0 and len(self.files) > 0:
            destination_dir = existing_directory('Choose where to save encrypted files')
            encrypt_files(self.files, destination_dir, self.public_key.text(), self.symmetric_algorithm_combobox.currentText())
            self.messageEncryptingFinished()
        else:
            message = ""
            if len(self.public_key.text()) == 0:
                message += 'You must provide path to public key\n'
            if len(self.files) == 0:
                message += 'You must choose files to encrypt\n'
            self.messageLackOfInput(message)

    def messageLackOfInput(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Warning')
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def messageEncryptingFinished(self):
        msg = QMessageBox()
        msg.setWindowTitle('Encrypting')
        msg.setText('Encrypting finished!')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
