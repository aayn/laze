from PyQt5.QtWidgets import (QMainWindow, QPushButton, QTextEdit,
                             QLabel, QInputDialog, qApp, QAction)
from PyQt5.QtGui import QFont, QColor, QIcon


class windowClass(QMainWindow):
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

        self.statusBar()
        self.statusBar().showMessage('Zzzzzzzzzzzzz...')

        self.setGeometry(0, 0, 800, 600)
        self.show()

    def initMenu(self):
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        fileMenu = menu.addMenu('&File')
        helpMenu = menu.addMenu('&Help')

        exitAction = QAction(QIcon('../images/exit.png'), '&Exit', self)
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

    def nameAsk(self):
        name, ok = QInputDialog.getText(self, 'Input Name',
                                        'Your name please? ')
        if ok:
            self.tedit.setText('Hello ' + str(name) +
                               '. Did you sleep well?')
