import sys
from WinFromApp import MainFrom
from WinFromApp import OpenFrom
from New import class1 as a
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainFrom.MainFrom()
    main.show()
    ch = OpenFrom.OpenFrom()
    table=a.Table()
    table.show()
    main.actionOpen.triggered.connect(ch.OPEN)
    sys.exit(app.exec_())
