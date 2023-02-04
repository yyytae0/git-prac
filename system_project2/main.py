from gui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainwidget()
    sys.exit(app.exec_())