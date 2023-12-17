import os
import sys
import platform
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QListView
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QProgressBar
from processor.select_from_files import SelectFromFiles
from processor.select_from_text import SelectFromText

ui_data = ''
if platform.system() == 'Windows':
    ui_data = os.path.join(os.getcwd(), 'resources/ui/app_window.ui')
else:
    exec_path = os.path.dirname(sys.executable)
    ui_data = os.path.join(exec_path, 'resources/ui/app_window.ui')
ui_class = uic.loadUiType(ui_data)[0]


class MainApp:
    def __init__(self):
        self.__application = QApplication(sys.argv)
        self.__window = MainWindow()

    def show(self):
        self.__window.show()

    def exec(self):
        self.__application.exec()


class MainWindow(QMainWindow, ui_class):
    def __init__(self):
        super().__init__()
        self.select_directory_path_edit: QLineEdit
        self.select_directory_path_edit = None
        self.target_directory_path_edit: QLineEdit
        self.target_directory_path_edit = None
        self.candidate_file_list: QListView
        self.candidate_file_list = None
        self.select_directory_button: QPushButton
        self.select_directory_button = None
        self.target_directory_button: QPushButton
        self.target_directory_button = None
        self.copy_button: QPushButton
        self.copy_button = None
        self.progress_bar: QProgressBar
        self.progress_bar = None
        self.__selected_path: str
        self.__selected_path = ''
        self.__target_path: str
        self.__target_path = ''

        self.setupUi(self)
        self.__bind()

    def __bind(self):
        self.select_directory_button.clicked.connect(self.__on_click_select)
        self.target_directory_button.clicked.connect(self.__on_click_target)
        self.copy_button.clicked.connect(self.__on_click_copy)

    def __on_click_select(self):
        self.__selected_path = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.select_directory_path_edit.setText(self.__selected_path)

    def __on_click_target(self):
        self.__target_path = QFileDialog.getExistingDirectory(self, 'Target Directory')
        self.target_directory_path_edit.setText(self.__target_path)

    def __on_click_copy(self):
        if not self.__is_valid():
            return

        selected_text_path = os.path.join(self.__selected_path, 'selected.txt')
        if os.path.exists(selected_text_path):
            SelectFromText.select(selected_text_path, self.__target_path, self.__on_update_progress)
        else:
            SelectFromFiles.select(self.__selected_path, self.__target_path, self.__on_update_progress)

    def __is_valid(self):
        if self.__selected_path == '' or self.__target_path == '':
            return False
        return True

    def __on_update_progress(self, ratio):
        self.progress_bar.setValue(int(ratio * 100))
