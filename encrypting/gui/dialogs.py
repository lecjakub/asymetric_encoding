from PyQt5.QtWidgets import QFileDialog
import ntpath

def existing_directory(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    directory = QFileDialog.getExistingDirectory(None, caption=caption, options=options)
    return directory

def save_file(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getSaveFileName(None, caption=caption, options=options)
    return filename

def file_from_path(path : str):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

