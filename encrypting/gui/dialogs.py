from PyQt5.QtWidgets import QFileDialog
import ntpath

def get_directory_to_save(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    directory = QFileDialog.getExistingDirectory(None, caption=caption, options=options)
    return directory

def get_file_to_save(caption):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getSaveFileName(None, caption=caption, options=options)
    return filename

def path_leaf(path : str):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

