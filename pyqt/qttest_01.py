import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

w = QWidget()
w.resize(250,150)
w.move(300,300)
w.setWindowTitle("Test1")
#w.showMaximized()
#w.showFullScreen()
w.show()

sys.exit(app.exec_())
