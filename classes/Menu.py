from PyQt5.QtWidgets import qApp, QMainWindow, QAction
from PyQt5.QtGui import QIcon


class Menu(QMainWindow):
    def initMenu(self):
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        fileMenu = menu.addMenu('&File')
        editMenu = menu.addMenu('&Edit')
        helpMenu = menu.addMenu('&Help')

        self.exitAction = QAction(QIcon('/home/aayn/Development/Python' +
                                        '/PyQt/laze/images/exit.png'),
                                        '&Exit', self)

        self.fontAction = QAction(QIcon('/home/aayn/Development/Python' +
                                        '/PyQt/laze/images/format.png'),
                                        '&Font', self)

        self.openAction = QAction(QIcon('/home/aayn/Development/Python' +
                                        '/PyQt/laze/images/open.png'),
                                        '&Open', self)

        self.saveAction = QAction(QIcon('/home/aayn/Development/Python' +
                                        '/PyQt/laze/images/save_blue.png'),
                                        '&Save', self)
        self.saveAction.setShortcut('Ctrl+S')

        self.exitAction.setStatusTip('Exit')
        self.fontAction.setStatusTip('Font')
        self.saveAction.setStatusTip('Save')
        self.openAction.setStatusTip('Open')
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        editMenu.addAction(self.fontAction)

        self.exitAction.triggered.connect(qApp.quit)
