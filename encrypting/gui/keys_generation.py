from PyQt5.QtWidgets import QVBoxLayout, QMessageBox , QInputDialog, QLabel, QDialogButtonBox,  QComboBox, QLineEdit, QApplication, QFormLayout, QDialog, QGroupBox
from PyQt5.QtCore import Qt
from encrypting.config import config
from encrypting.gui.helpers import existing_directory
from encrypting.logic.algorithms import generate_asymmetric_key

class AsymmetricKeyGenerationDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = QLineEdit()
        self.algorithm_combobox = QComboBox()
        self.algorithm_combobox.addItems(config['algorithms']['asymmetric'])
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Save)
        buttonBox.accepted.connect(self.saveKeys)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Asymmetric key generation")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Creating asymmetric key")
        layout = QFormLayout()
        layout.addRow(QLabel("Key filename:"), self.filename)
   
        layout.addRow(QLabel("Algorithm:"), self.algorithm_combobox)
        self.formGroupBox.setLayout(layout)

    def saveKeys(self):
        if len(self.filename.text()) == 0:
            self.messageNoFileNameTyped()
            return

        dirpath = existing_directory("Choose where to save your keys")
        if dirpath:
            asymm_key = generate_asymmetric_key(self.algorithm_combobox.currentText())
            with open(dirpath + '/' + self.filename.text(), "wb") as private_key_file:          
                private_key_file.write(asymm_key.private_to_bytes())
            with open(dirpath + '/' + self.filename.text()+ '.pub', "wb") as public_key_file:
                public_key_file.write(asymm_key.public_to_bytes())
            # self.close()
        

    def messageNoFileNameTyped(self):
        msg = QMessageBox()
        msg.setWindowTitle('Warning')
        msg.setText('Type filename first!')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()