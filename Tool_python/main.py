import os

os.system("pip3 install pandas") #실행되면 패키지가 자동적으로 다운로드
os.system("pip3 install PyQt5")

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from dataset import get_data
from problem import make

from process import DlgProcess
from result import DlgResult

font1 = QFont("Arial", 24)
font1.setBold(True)

font2 = QFont("Arial", 15) #15

font3 = QFont("Arial", 15) #15
font3.setBold(True)

class WdgPgmMain(QWidget):
    idx = 0   # 제시어 종류 인덱스
    num = 0  # 제시어 개수
    time = 0   # 제시어 노출 시간(초)
    length = 0  # 제시어 길이

    def __init__(self):
        super().__init__()

        vbox1 = QVBoxLayout()

        lblTitle = QLabel('Magic Number Program')
        lblTitle.setFont(font1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(lblTitle)
        hbox1.addStretch(1)

        self.rdbH = QRadioButton('한글')
        self.rdbH.setFont(font2)
        self.rdbH.clicked.connect(self.radioButton_clicked)
        self.rdbH.setChecked(True)

        self.rdbH_O = QRadioButton('한글(받침 O)')
        self.rdbH_O.setFont(font2)
        self.rdbH_O.clicked.connect(self.radioButton_clicked)

        self.rdbH_X = QRadioButton('한글(받침 X)')
        self.rdbH_X.setFont(font2)
        self.rdbH_X.clicked.connect(self.radioButton_clicked)

        self.rdbE = QRadioButton('영어')
        self.rdbE.setFont(font2)
        self.rdbE.clicked.connect(self.radioButton_clicked)

        self.rdbN = QRadioButton('숫자')
        self.rdbN.setFont(font2)
        self.rdbN.clicked.connect(self.radioButton_clicked)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.rdbH)
        vbox2.addStretch(1)
        vbox2.addWidget(self.rdbH_O)
        vbox2.addStretch(1)
        vbox2.addWidget(self.rdbH_X)
        vbox2.addStretch(1)
        vbox2.addWidget(self.rdbE)
        vbox2.addStretch(1)
        vbox2.addWidget(self.rdbN)

        vbox3 = QVBoxLayout()

        lblCount = QLabel('제시어 개수')
        lblCount.setFont(font3)

        self.ledCount = QLineEdit()
        self.ledCount.setFont(font3)
        self.ledCount.setText('5')
        self.ledCount.setAlignment(Qt.AlignRight)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(lblCount)
        hbox4.addStretch(1)
        hbox4.addWidget(self.ledCount)

        lblTime = QLabel('제시어 노출 시간(초)')
        lblTime.setFont(font3)

        self.ledTime = QLineEdit()
        self.ledTime.setFont(font3)
        self.ledTime.setText('5')
        self.ledTime.setAlignment(Qt.AlignRight)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(lblTime)
        hbox5.addWidget(self.ledTime)

        lblLength = QLabel('제시어 길이')
        lblLength.setFont(font3)

        self.ledLength = QLineEdit()
        self.ledLength.setFont(font3)
        self.ledLength.setText('3')
        self.ledLength.setAlignment(Qt.AlignRight)

        hbox6 = QHBoxLayout()
        hbox6.addWidget(lblLength)
        hbox6.addStretch(1)
        hbox6.addWidget(self.ledLength)

        vbox3.addLayout(hbox4)
        vbox3.addStretch(1)
        vbox3.addLayout(hbox5)
        vbox3.addStretch(1)
        vbox3.addLayout(hbox6)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addLayout(vbox2)
        hbox2.addStretch(1)
        hbox2.addLayout(vbox3)
        hbox2.addStretch(1)

        pbtnStart = QPushButton('시작')
        pbtnStart.setFont(font3)
        pbtnStart.clicked.connect(self.pbtnStart_clicked)

        pbtnEnd = QPushButton('종료')
        pbtnEnd.setFont(font3)
        pbtnEnd.clicked.connect(self.pbtnEnd_clicked)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(15)
        hbox3.addWidget(pbtnStart)
        hbox3.addStretch(1)
        hbox3.addWidget(pbtnEnd)
        hbox3.addStretch(2)

        vbox1.addStretch(1)
        vbox1.addLayout(hbox1)
        vbox1.addStretch(1)
        vbox1.addLayout(hbox2)
        vbox1.addStretch(1)
        vbox1.addLayout(hbox3)
        vbox1.addStretch(1)

        self.setLayout(vbox1)
        self.setGeometry(300, 100, 800, 500)
        self.setWindowTitle('Magic Number')
        self.show()

    def radioButton_clicked(self):
        if self.rdbH.isChecked():
            self.idx = 0
        elif self.rdbH_O.isChecked():
            self.idx = 1
        elif self.rdbH_X.isChecked():
            self.idx = 2
        elif self.rdbE.isChecked():
            self.idx = 3
        elif self.rdbN.isChecked():
            self.idx = 4

    def pbtnStart_clicked(self):
        data = get_data()

        num = int(self.ledCount.text())   # 제시어 개수
        time = float(self.ledTime.text())   # 제시어 노출 시간(초)
        length = int(self.ledLength.text())   # 제시어 길이

        problems = make(data, self.idx, num, length)

        self.hide()
        dlgProcess = DlgProcess(problems, num, time, length)
        dlgProcess.exec()
        self.show()

    def closeEvent(self, event):
        sys.exit()

    def pbtnEnd_clicked(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = WdgPgmMain()
    sys.exit(app.exec_())