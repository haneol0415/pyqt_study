import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import urllib.request

from_class = uic.loadUiType("painter.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Painter")

        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)

        self.label.setPixmap(self.pixmap)
        self.x, self.y = None, None
        self.click = None
        
        # self.draw()

        # self.painter = QPainter(self.label.pixmap())

    
    def mouseMoveEvent(self, event):
        diff = 0
        x = event.x() - diff
        y = event.y() - diff
        
        if self.x is None:
            self.x = x
            self.y = y
            return
        
        self.point_pos.setText(": local({0}, {1}), global(({2}, {3}))".format(x, y, event.globalX(), event.globalY()))
        
        painter = QPainter(self.label.pixmap())
        painter.drawLine(self.x, self.y, x, y)
        painter.end()
        self.update()

        self.x = x
        self.y = y
        
        
        
    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.point_press.setText(": Left")
        elif event.buttons() & Qt.RightButton:
            self.point_press.setText(": Right")
        else:
            self.point_press.setText(": Middle")

    def wheelEvent(self, event):
        text = "{0}, {1}".format(event.angleDelta().x(), event.angleDelta().y())
        self.mouse_wheel.setText(text)


    
    def mouseReleaseEvent(self, event):
        self.x  = None
        self.y  = None
    
    
    def draw(self):
        painter = QPainter(self.label.pixmap())

        self.pen = QPen(Qt.red, 5, Qt.SolidLine)
        painter.setPen(self.pen)
        painter.drawLine(100, 100, 500, 100)
        
        self.pen.setBrush(Qt.blue)
        self.pen.setWidth(10)
        self.pen.setStyle(Qt.DashDotLine)
        painter.setPen(self.pen)
        self.line = QLine(100 ,200, 500,  200)
        painter.drawLine(self.line)

        painter.setPen(QPen(Qt.black, 20, Qt.DotLine))
        self.p1 = QPoint(100, 300)
        self.p2 = QPoint(500, 300)
        painter.drawLine(self.p1, self.p2)

        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(100, 10, 100, 50)

        painter.drawEllipse(350, 350, 100, 100)

        self.font = QFont()
        self.font.setFamily("Times")
        self.font.setBold(True)
        self.font.setPointSize(20)
        painter.setFont(self.font)
        painter.drawText(100, 400, "This is draw Text")
        
        painter.end


        
        
    
    
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())