import sys
from PyQt5.QtWidgets import (QWidget, QGraphicsView,
    QPushButton, QApplication, QLabel)
from PyQt5.QtCore import (QTimer, QTime)
from PyQt5.QtGui import QColor
import random



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        self.col = QColor(0, 0, 0)

        self.btn = QPushButton('Start', self)
        self.btn.move(320, 500)
        self.btn.clicked.connect(self.doAction)
        self.btn.resize(150, 100)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.step = 0
        self.lbl = QLabel(self)
        self.lbl1 = QLabel(self)
        self.setWindowTitle('QProgressBar')

        self.square = QGraphicsView(self)
        self.square.setGeometry(200, 50, 350, 350)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.col.name())
        self.lbl.move(320, 450)
        self.lbl1.move(470, 450)
        self.setGeometry(400, 150, 800, 800)
        self.lbl.setText('0')
        self.lbl.adjustSize()
        self.lbl1.setText('1')
        self.lbl1.adjustSize()
        self.k = 0
        self.min = 1
        self.timer.timeout.connect(self.doAct)
        self.show()
    def doAct(self):
        self.col.setRgb(0, 255, 0)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())
        self.time1 = QTime.currentTime()
        self.k = 2
        self.btn.setText('Press')
        self.timer.stop()

    def doAction(self):
        if self.k == 0:
            self.timer.start(random.randint(2, 4) * 1000)
            self.btn.setText('Ready')
            self.k = 1
        elif self.k == 1:
            self.btn.setText('Stoped')
            self.lbl.setText('End')
            self.timer.stop()
            self.k = 3
        elif self.k == 2:
            self.btn.setText('Finish')
            self.time2 = QTime.currentTime()

            self.time = str((self.time2.second() * 1000 + self.time2.msec() - self.time1.second() * 1000 - self.time1.msec()) // 1000) + '.' + str((self.time2.second() * 1000 + self.time2.msec() - self.time1.second() * 1000 - self.time1.msec()) % 1000)
            self.lbl.setText(self.time)
            if float(self.time) < self.min:
                self.lbl1.setText(self.time)
                self.lbl1.adjustSize()
                self.min = float(self.time)
            self.lbl.adjustSize()
            self.col.setRgb(0, 255, 255)
            self.square.setStyleSheet("QWidget { background-color: %s }" %
                                      self.col.name())
            self.k = 3
        else:
            self.timer.start(random.randint(1, 15) * 1000)
            self.col = QColor(0, 0, 0)
            self.square.setStyleSheet("QWidget { background-color: %s }" %
                                      self.col.name())
            self.btn.setText('Ready')
            self.k = 1


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())