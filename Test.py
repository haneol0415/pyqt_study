import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("Test.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test, PyQt!")
        
        self.pushButton_1.clicked.connect(self.button1_Clicked)
        self.pushButton_2.clicked.connect(self.button2_Clicked)
        self.pushButton_3.clicked.connect(self.button3_Clicked)

        self.radio_1.clicked.connect(self.radioClicked)
        self.radio_2.clicked.connect(self.radioClicked)
        self.radio_3.clicked.connect(self.radioClicked)

    def radioClicked(self):
        if self.radio_1.isChecked():
            self.textEdit.setText("Radio_1")
        elif self.radio_2.isChecked():
            self.textEdit.setText("Radio_2")
        elif self.radio_3.isChecked():
            self.textEdit.setText("Radio_3")
        else:
            self.textEdit.setText("Unkonwn")
    
    def button1_Clicked(self):
        self.textEdit.setText("Button 1")
        self.radio_1.setChecked(True)
    
    def button2_Clicked(self):
        self.textEdit.setText("Button 2")
        self.radio_2.setChecked(True)

    def button3_Clicked(self):
        self.textEdit.setText("Button 3")
        self.radio_3.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())