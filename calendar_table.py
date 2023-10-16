import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from datetime import datetime

from_class = uic.loadUiType("Calendar.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ComboBox")
        
        
        self.cbGender.addItem("성별 선택")
        self.cbGender.addItem("F")
        self.cbGender.addItem("M")
        self.cbGender.setCurrentText("성별 선택")
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnAdd.clicked.connect(self.Add)
        self.btnDelete.clicked.connect(self.Delete)

    def Add(self):
        name = self.editName.text()
        gender = self.cbGender.currentText()
        if name != "" and gender != "성별 선택":
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(self.editName.text()))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.cbGender.currentText()))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(self.editBirthday.text()))
            self.editName.setText("")
            self.cbGender.setCurrentText("성별 선택")
      
    def Delete(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.removeRow(row - 1)
        

    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())