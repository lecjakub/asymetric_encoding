from __future__ import unicode_literals

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGridLayout, QHBoxLayout, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from config import config

class KeyGenModel(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.layout : QGridLayout= None
        self.cb : QComboBox= None
        self.setup()



    def setup(self):
        self.layout = QGridLayout()
        cb_label = QLabel("Choose asymmetric algorithm")
        self.layout.addWidget(cb_label, 0, 0)

        self.cb = QComboBox()
        self.cb.addItems(config['algorithms']['asymmetric'])
        # self.cb.currentIndexChanged.connect(self.)
        self.layout.addWidget(self.cb, 0, 1)

        gen_button = QPushButton("Generate key")
        gen_button.clicked.connect(self.generate_asymmetric_key)
        self.layout.addWidget(gen_button, 2, 1)

    def generate_asymmetric_key(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        raise NotImplemented



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

        self.initUI()
        self.layout = None

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        vbox = QVBoxLayout()
        vbox.addLayout(self.keyGenModel.layout)
        vbox.addLayout(self.createEncryptingBox())
        vbox.addLayout(self.createDecryptingBox())
        self.setLayout(vbox)
        # with open('style.css') as styles:
        #     self.setStyleSheet(styles.read())
        self.show()


    def createEncryptingBox(self):
        hbox = QHBoxLayout()
        okButton = QPushButton("OK")
        hbox.addWidget(okButton)
        return hbox


    def createDecryptingBox(self):
        hbox = QHBoxLayout()
        okButton = QPushButton("OK")
        hbox.addWidget(okButton)
        return hbox

    def generate_key_callback(self):
        print("gen key clicked")

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
