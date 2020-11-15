import sys

if r"D:\Artfx\GarciaTD4\Python-DCC\ib" not in sys.path:
    sys.path.append(r'D:\Artfx\GarciaTD4\Python-DCC\lib')
    sys.path.append(r'D:\Artfx\GarciaTD4\Python-DCC\pipeline')

from Qt import QtWidgets, QtCompat
from pipeline.ui import my_window as mw

app = QtWidgets.QApplication(sys.argv)

win = mw.MyWindow()
win.show()

sys.exit(app.exec_())