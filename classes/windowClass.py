from PyQt5.QtWidgets import (QMainWindow, QPushButton, QTextEdit,
                             QLabel, QInputDialog, QAction)
from PyQt5.QtGui import QFont, QColor, QIcon
from classes.Menu import Menu
from classes.Dialogs import Dialogs


class windowClass(Menu, Dialogs):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('Laze Text Editor')
        self.name = QLabel('Too lazy to ask for your name again.',
                           self)
        self.tedit = QTextEdit('Too lazy to ask for your name again.')
        self.setCentralWidget(self.tedit)
        self.nameAsk()

        self.initMenu()

        self.fontAction.triggered.connect(self.fontDialog)
        self.saveAction.triggered.connect(self.saveDialog)
        self.openAction.triggered.connect(self.openDialog)

        self.statusBar()
        self.statusBar().showMessage('Zzzzzzzzzzzzz...')

        self.setGeometry(0, 0, 800, 600)
        self.show()
