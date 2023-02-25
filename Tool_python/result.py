import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

from accuracy import ac
from excel import excel

font1 = QFont("Arial", 24)
font1.setBold(True)

font2 = QFont("Arial", 15)
font2.setBold(True)

class DlgResult(QDialog):
    def __init__(self, problems, listAnswers):
        super().__init__()

        self.problems = problems
        self.listAnswers = listAnswers

        lblResult = QLabel('결과')
        lblResult.setFont(font1)
        lblResult.setAlignment(Qt.AlignCenter)

        pbtnExcel = QPushButton('엑셀 파일로 저장')
        pbtnExcel.setFixedWidth(190)
        pbtnExcel.setFont(font2)
        pbtnExcel.clicked.connect(self.pbtnExcel_clicked)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(lblResult)
        hbox1.addWidget(pbtnExcel)

        self.tblResult = QTableWidget()
        self.tblResult.setFont(font2)

        pbtnReStart = QPushButton('다시 시작')
        pbtnReStart.setFixedWidth(120)
        pbtnReStart.setFont(font2)
        pbtnReStart.clicked.connect(self.pbtnReStart_clicked)

        pbtnEnd = QPushButton('종료')
        pbtnEnd.setFont(font2)
        pbtnEnd.clicked.connect(self.pbtnEnd_clicked)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(pbtnReStart)
        hbox2.addWidget(pbtnEnd)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.tblResult)
        vbox1.addLayout(hbox2)

        self.setLayout(vbox1)
        self.setGeometry(300, 100, 800, 500)
        self.setWindowTitle('Result Form')
        self.show()

        self.resultView()

    def resultView(self):
        self.tblResult.setColumnCount(3)
        listHeaders = ["제시어", "입력 단어", "일치율"]
        self.tblResult.setHorizontalHeaderLabels(listHeaders)
        self.tblResult.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   # 창 너비에 비례해서 조정됨

        self.listAc = ac(self.problems, self.listAnswers)

        self.tblResult.setRowCount(len(self.problems))

        for row in range(len(self.problems)):
            self.tblResult.setItem(row, 0, QTableWidgetItem(self.problems[row]))
            self.tblResult.setItem(row, 1, QTableWidgetItem(self.listAnswers[row]))
            self.tblResult.setItem(row, 2, QTableWidgetItem(self.listAc[row]))

            for col in range(3):
                self.tblResult.item(row, col).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)   # 각 셀 수평, 수직 가운데 정렬

    def pbtnExcel_clicked(self):
        excel(self.problems, self.listAnswers, self.listAc)

    def pbtnReStart_clicked(self):
        self.close()

    def pbtnEnd_clicked(self):
        sys.exit()