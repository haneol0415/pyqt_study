import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("Test2.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test2")

        self.count = 0
        self.min = 0
        self.max = 10
        self.di = 1
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.reset)

        self.label.setText(str(self.count))

    def buttonClicked(self):
        if self.count == self.min:
            self.di = 1
        elif self.count == self.max:
            self.di = 0
        else:
            pass
        
        if self.di == 1:
            self.count += 1
        else:
            self.count -= 1

        self.label.setText(str(self.count))
    
    def reset(self):
        self.count = 0
        self.di = 0
        self.label.setText(str(self.count))

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())


