import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit it!', self)
        #qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.close)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        resize_btn = QPushButton('Resize!', self)
        resize_btn.clicked.connect(self.resizeTheWindow)
        resize_btn.resize(resize_btn.sizeHint())
        resize_btn.move(100,100)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

    def resizeTheWindow(self):
        self.resize(500, 500)
        self.center()

    def center(self):

        qr = self.frameGeometry()
        print qr
        cp = QDesktopWidget().availableGeometry().center()
        print cp
        qr.moveCenter(cp)
        print qr
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())