from __future__ import unicode_literals
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGridLayout, QHBoxLayout, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtGui import QIcon
from config import config


class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.title = config['gui']['name']
        self.left = config['gui']['x']
        self.top = config['gui']['y']
        self.width = config['gui']['width']
        self.height = config['gui']['height']
        self.vbox = None

        self.initUI()
        self.layout = None

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setFixedSize(self.width, self.height)

        vbox = QVBoxLayout()
        self.initKeyGen(vbox)
        self.initEncryptingArea(vbox)
        self.initDecryptingArea(vbox)
        self.setLayout(vbox)
        with open('style.css') as styles:
            self.setStyleSheet(styles.read())
        self.show()

    def initKeyGen(self, parent: QVBoxLayout):
        grid = QGridLayout()
        assymetric_combo = QComboBox()
        symmetric_combo = QComboBox()
        [assymetric_combo.addItem(item) for item in config['algorithms']['asymmetric']]
        [symmetric_combo.addItem(item) for item in config['algorithms']['symmetric']]
        grid.addWidget(assymetric_combo, 0, 0)
        grid.addWidget(symmetric_combo, 0, 1)
        parent.addLayout(grid)

    def initEncryptingArea(self, parent: QVBoxLayout):
        hbox = QHBoxLayout()
        okButton = QPushButton("OK")
        hbox.addWidget(okButton)
        parent.addLayout(hbox)


    def initDecryptingArea(self, parent: QVBoxLayout):
        hbox = QHBoxLayout()
        okButton = QPushButton("OK")
        hbox.addWidget(okButton)
        parent.addLayout(hbox)


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
