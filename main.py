import sys
from PyQt5.QtWidgets import QApplication
from classes.windowClass import windowClass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    foo = windowClass()
    sys.exit(app.exec_())
