from tracemalloc import start
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from route import *
import sys

class mainwidget(QWidget):

    def __init__(self):
        super().__init__()
        self.data = read_data()
        self.path = findpath(self.data) 
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Start:'), 0, 0)
        grid.addWidget(QLabel('Dest:'), 1, 0)
        grid.addWidget(QLabel('Route:'), 2, 0)
        self.btn = QPushButton('&Button1')
        self.btn.setText('Run')	
        grid.addWidget(self.btn, 3,0)

        self.start = QLineEdit(self)
        self.dest = QLineEdit(self)
        self.route = QTextBrowser(self)
        grid.addWidget(self.start, 0, 1)
        grid.addWidget(self.dest, 1, 1)
        grid.addWidget(self.route, 2, 1)

        self.btn.clicked.connect(self.run)

        self.setWindowTitle('Prototype')
        self.setGeometry(300, 300, 500, 400)

        self.show()

    def run(self):
        start = int(self.start.text())
        dest = int(self.dest.text())
        ro = self.path.dfs(start,dest)
        text = "Cost: " + str(ro[0]) + "\nRoute: "
        for i in ro[1]:
            text += str(i)
            text += " -> "
        text = text[:-3]
        self.path.reset()
        self.route.setText(text)