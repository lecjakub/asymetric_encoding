from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLineEdit, QGroupBox, QFormLayout, QVBoxLayout, QLabel, QPushButton, QMessageBox
from encrypting.gui.helpers import existing_directory, open_multiple_files, open_file, validate_key_size
from encrypting.logic.core import decrypt_files
class DecryptionDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.privateKey = QLineEdit()
        self.privateKey.setPlaceholderText('Path to private key file')
        self.filesCounter = QLabel("Files loaded: 0")
        self.files = []
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        buttonBox.button(QDialogButtonBox.Ok).setText('Decrypt')
        buttonBox.accepted.connect(self.decrypt)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

    def reject(self):
        """To avoid closing on esc press"""
        pass

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Decryption")
        layout = QFormLayout()
        loadFilesButton = QPushButton('Load files to decrypt')
        loadFilesButton.clicked.connect(self.loadFiles)
        layout.addRow(self.filesCounter, loadFilesButton)
        loadPrivateKeyButton = QPushButton('Load private key')
        loadPrivateKeyButton.clicked.connect(self.loadPrivateKey)
        layout.addRow(self.privateKey, loadPrivateKeyButton)
        self.formGroupBox.setLayout(layout)

    def loadFiles(self):
        self.files = open_multiple_files('Choose files to decrypt')
        if len(self.files) > 0:
            self.filesCounter.setText('Files loaded: %d' % len(self.files))

    def loadPrivateKey(self):
        filename = open_file('Open private key file')
        if filename is not None:
            self.privateKey.setText(filename)


    def decrypt(self):
        if len(self.files) > 0 and len(self.privateKey.text()) > 0:
            if not validate_key_size(self.privateKey.text()):
                return
            destination_dir = existing_directory('Choose where to save decrypted files')
            if destination_dir:
                decrypt_files(self.files, destination_dir, self.privateKey.text())

        else:
            message = ''
            if len(self.privateKey.text()) == 0:
                message += 'You must provide path to private key\n'
            if len(self.files) == 0:
                message += 'You must choose files to decrypt\n'
            self.messageLackOfInput(message)

    def messageLackOfInput(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Warning')
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def messageDecryptingFinished(self):
        msg = QMessageBox()
        msg.setWindowTitle('Decrypting')
        msg.setText('Decrypting finished!')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()