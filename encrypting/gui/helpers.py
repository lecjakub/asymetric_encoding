from PyQt5.QtWidgets import QFileDialog
import ntpath
import os
from PyQt5.QtWidgets import QMessageBox
def existing_directory(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    directory = QFileDialog.getExistingDirectory(None, caption=caption, options=options)
    return directory

def open_file(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getOpenFileName(None, caption=caption, options=options)
    return filename

def open_multiple_files(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    files = QFileDialog.getOpenFileNames(None, caption=caption, options=options)
    return files[0]

def save_file(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getSaveFileName(None, caption=caption, options=options)
    return filename

def file_from_path(path : str):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def validate_key_size(path:str):
    ksize = os.path.getsize(path)
    valid = ksize == 520 or ksize == 1032
    if not valid:
        messageInvalidKeySize()
    return valid


def messageInvalidKeySize():
        msg = QMessageBox()
        msg.setWindowTitle('Warning')
        msg.setText("Key is invalid!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
