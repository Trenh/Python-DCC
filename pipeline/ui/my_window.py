import sys, os

sys.path.append(r'D:/Artfx/GarciaTD4/Python-DCC/lib')

from Qt import QtWidgets, QtCompat
from pipeline.engine import engine

ui_path = os.path.join(os.path.dirname(__file__), "my_window.ui")

class MyWindow(QtWidgets.QMainWindow):

    engine_name = engine.get_current()

    def __init__(self):
        
        super(MyWindow, self).__init__()
        QtCompat.loadUi(ui_path, self)
        self.open_button.clicked.connect(self.open)
        self.save_button.clicked.connect(self.save)
        self.export_button.clicked.connect(self.export)
        self.import_button.clicked.connect(self.importation)

    def open(self, path):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "C:\\Users\\luffy\\Documents")
        self.engine_name.open(filename[0])

    def save(self):
        self.engine_name.save()
    def export(self):
        print('Export button clicked')
        search_namespace = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\luffy\\Documents")
        self.name_export.setText(search_namespace[0])
        in_file = self.name_export.text()
        print("Extracting Namespace in " + in_file )

        self.engine_name.export(in_file)

    def importation(self):
        print("import button clicked")
        search_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory", "D:\\Artfx\\GarciaTD4\\Python-DCC\\export")
        self.import_directory.setText(search_dir)
        directory = self.import_directory.text()

        self.engine_name.importation(directory)
