import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("textbrowser.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TextBrowser, Qt!")
        
        self.addButton.clicked.connect(self.add_Clicked)
        self.clearButton.clicked.connect(self.clear_Clicked)
        self.lineEdit.returnPressed.connect(self.add_Clicked)

    def add_Clicked(self):
        input = self.lineEdit.text()
        self.lineEdit.clear()
        self.textBrowser.append(input)
    
    def clear_Clicked(self):
        self.lineEdit.clear()
        self.textBrowser.clear()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())