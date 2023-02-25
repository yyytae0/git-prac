import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

from result import DlgResult

font1 = QFont("Arial", 24)
font1.setBold(True)

font2 = QFont("Arial", 15)
font2.setBold(True)

class DlgProcess(QDialog):
    def __init__(self, problems, suggNum, suggExpSec, sussLength):
        super().__init__()

        self.problems = problems
        self.suggNum = suggNum
        self.suggExpSec = suggExpSec
        self.sussLength = sussLength

        self.isInputApply = False
        self.finishable = True
        self.listAnswers = []

        self.lblSuggest = QLabel('제시어')
        self.lblSuggest.setFont(font1)

        self.ledSuggest = QLineEdit()
        self.ledSuggest.resize(500, 30)
        self.ledSuggest.setAlignment(Qt.AlignCenter)
        self.ledSuggest.setFont(font1)
        self.ledSuggest.setStyleSheet('color : blue')
        self.ledSuggest.setReadOnly(True)
        self.ledSuggest.setText(problems[0])

        self.lblSecond = QLabel('%.1f' % suggExpSec)
        self.lblSecond.setFixedWidth(100)
        self.lblSecond.setAlignment(Qt.AlignCenter)
        self.lblSecond.setFont(font1)
        self.lblSecond.setStyleSheet('color : brown')

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.lblSuggest)
        hbox1.addStretch(1)
        hbox1.addWidget(self.ledSuggest)
        hbox1.addStretch(1)
        hbox1.addWidget(self.lblSecond)
        hbox1.addStretch(1)

        self.lblAnswer = QLabel('답입력')
        self.lblAnswer.setFont(font1)
        self.lblAnswer.setVisible(False)

        self.ledAnswer = QLineEdit()
        self.ledAnswer.setAlignment(Qt.AlignCenter)
        self.ledAnswer.setFont(font1)
        self.ledAnswer.setMaxLength(sussLength)
        self.ledAnswer.setVisible(False)
        self.ledAnswer.textChanged.connect(self.ledAnswer_textChanged)
        self.ledAnswer.returnPressed.connect(self.pbtnInput_clicked)

        self.pbtnInput = QPushButton('입력')
        self.pbtnInput.setFixedWidth(100)
        self.pbtnInput.setFont(font1)
        self.pbtnInput.setVisible(False)
        self.pbtnInput.setEnabled(False)
        self.pbtnInput.clicked.connect(self.pbtnInput_clicked)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.lblAnswer)
        hbox2.addStretch(1)
        hbox2.addWidget(self.ledAnswer)
        hbox2.addStretch(1)
        hbox2.addWidget(self.pbtnInput)
        hbox2.addStretch(1)

        pbtnEnd = QPushButton('종료')
        pbtnEnd.setFont(font2)
        pbtnEnd.clicked.connect(self.pbtnEnd_clicked)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(15)
        hbox3.addWidget(pbtnEnd)
        hbox3.addStretch(1)

        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setRange(0, suggNum)
        self.progressBar.setValue(1)

        self.lblCount = QLabel(f'1 / {suggNum}')
        self.lblCount.setFont(font2)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.progressBar)
        hbox4.addWidget(self.lblCount)

        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addLayout(hbox1)
        vbox1.addStretch(1)
        vbox1.addLayout(hbox2)
        vbox1.addStretch(1)
        vbox1.addLayout(hbox3)
        vbox1.addStretch(1)
        vbox1.addLayout(hbox4)
        vbox1.addStretch(1)

        self.setLayout(vbox1)
        self.setGeometry(300, 100, 800, 500)
        self.setWindowTitle('Magic Number')
        self.show()

        self.remaNum = self.suggNum
        self.remaExpSec = self.suggExpSec

        self.timer1 = QTimer(self)
        self.timer1.start(100)
        self.timer1.timeout.connect(self.secondCount)

    def secondCount(self):
        self.remaExpSec -= 0.1
        self.lblSecond.setText('%.1f' % self.remaExpSec)

        if self.remaExpSec <= 0:
            self.timer1.stop()
            self.lblSecond.setText('0.0')
            self.isInputApply = False

            if self.remaNum > 0:
                self.lblSuggest.setVisible(False)
                self.ledSuggest.setVisible(False)
                self.lblSecond.setVisible(False)

                self.ledSuggest.setText('')
                self.lblAnswer.setVisible(True)
                self.ledAnswer.setVisible(True)
                self.pbtnInput.setVisible(True)
                self.ledAnswer.setFocus()

    # def closeEvent(self, event):
    #     if self.finishable: sys.exit()
    #     self.finishable = True

    def ledAnswer_textChanged(self):
        if len(self.ledAnswer.text()) == self.sussLength:
            self.pbtnInput.setEnabled(True)
        else:
            self.pbtnInput.setEnabled(False)

    def pbtnInput_clicked(self):
        if not self.isInputApply:
            if len(self.ledAnswer.text()) != self.sussLength: return

            self.isInputApply = True

            self.listAnswers.append(self.ledAnswer.text())

            if self.remaNum >= 2:
                self.remaNum -= 1
                self.remaExpSec = self.suggExpSec

                self.ledSuggest.setText(self.problems[self.suggNum - self.remaNum])
                self.progressBar.setValue(self.suggNum - self.remaNum + 1)
                self.lblCount.setText(f'{self.suggNum - self.remaNum + 1} / {self.suggNum}')

                self.lblSuggest.setVisible(True)
                self.ledSuggest.setVisible(True)
                self.lblSecond.setVisible(True)

                self.ledAnswer.setText('')
                self.lblAnswer.setVisible(False)
                self.ledAnswer.setVisible(False)
                self.pbtnInput.setVisible(False)

                self.timer1.start(100)
            else:   # 결과 창을 띄우고 테이블로 결과 값을 보여준다
                self.close()
                dlgResul = DlgResult(self.problems, self.listAnswers)
                dlgResul.exec()

        self.finishable = False

    def pbtnEnd_clicked(self):
        if self.finishable: sys.exit()
        self.finishable = True
