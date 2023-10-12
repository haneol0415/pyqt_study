import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("textbrowser2.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TextBrowser2, Qt!")
        
        self.Add.clicked.connect(self.addText)
        self.Clear.clicked.connect(self.clearText)
        self.FontUbuntu.clicked.connect(lambda: self.setFont("Ubuntu"))
        self.FontNanumGothic.clicked.connect(lambda: self.setFont("NanumGothic"))

        self.Red.clicked.connect(lambda: self.setTextColor(255, 0, 0))
        self.Green.clicked.connect(lambda: self.setTextColor(0, 255, 0))
        self.Blue.clicked.connect(lambda: self.setTextColor(0, 0, 255))

        self.SetFontSize.clicked.connect(self.setFontSize)

        self.FontSize.textChanged.connect(self.checkDigit)
        self.FontSize.returnPressed.connect(self.setFontSize)
        # self.FontSize.setValidator(QIntValidator())
        

    def clearText(self):
        self.Input.clear()
        self.Output.clear()

    def addText(self):
        input = self.Input.toPlainText()
        self.Input.clear()
        self.Output.append(input)
    
    def setFont(self, fontName):
        font = QFont(fontName, 11)
        self.Output.setFont(font)

    def setTextColor(self, r, g, b):
        color = QColor(r, g, b)
        self.Output.selectAll()
        self.Output.setTextColor(color)
        self.Output.moveCursor(QTextCursor.End)

    def setFontSize(self):
        size = int(self.FontSize.text())
        self.Output.selectAll()
        self.Output.setFontPointSize(size)
        self.Output.moveCursor(QTextCursor.End)

    def checkDigit(self):
        text = self.FontSize.text()
        if text.isdigit() == False:
            self.FontSize.setText(text[:-1])




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())