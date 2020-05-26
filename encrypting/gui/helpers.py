from PyQt5.QtWidgets import QFileDialog
import ntpath

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

