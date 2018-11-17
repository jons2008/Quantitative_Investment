import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from New import class1 as aa
if __name__ == '__main__':
    app=QApplication(sys.argv)
    table=aa.Table()
    table.show()
    sys.exit(app.exec_())