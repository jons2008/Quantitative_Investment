import sys
from PyQt5.QtWidgets import qApp, QAction, QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from New import class1 as cl
class Menu_From(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar()

        exitAction = QAction('&', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit)

        exitAction1 = QAction('&Exit', self)
        exitAction1.setShortcut('Ctrl+Q')
        exitAction1.setStatusTip('Exit app')
        exitAction1.triggered.connect(self.Open_Data)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&file')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(exitAction1)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('menubar')
        self.show()

    def Open_Data(self):
        app=QApplication(sys.argv)
        c=cl.Table()
        c.show()