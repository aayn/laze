from PyQt5.QtWidgets import QWidget, QInputDialog, QFontDialog, QFileDialog
import os


class Dialogs(QWidget):
    def nameAsk(self):
        name, ok = QInputDialog.getText(self, 'Input Name',
                                        'Your name please? ')
        if ok:
            self.tedit.setText('Hello ' + str(name) +
                               '. Did you sleep well?')

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tedit.setFont(font)

    def saveDialog(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File',
                                               os.getenv('HOME'))[0]
        f = open(filename, 'w')
        tedittext = self.tedit.toPlainText()
        f.write(tedittext)
        f.close()

    def openDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File',
                                               os.getenv('HOME'))[0]
        self.setWindowTitle('Laze Text Editor - ' + filename)
        f = open(filename, 'ra')
        self.tedit.setText(f.read())
        f.close()
