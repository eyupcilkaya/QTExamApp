import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication
import variables
import main_win
import load_win
import question_win
import info_win

v = variables.Variables()


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        widget = QtWidgets.QStackedWidget()

        v.setWidget(widget)
        main_window = main_win.MainWindow(v)
        quest_window = question_win.QuestionWindow(v)
        info_window = info_win.InfoWindow(v)
        load_window = load_win.LoadWindow(v)

        widget.addWidget(main_window)
        widget.addWidget(quest_window)
        widget.addWidget(load_window)
        widget.addWidget(info_window)

        widget.setFixedWidth(800)
        widget.setFixedHeight(600)
        widget.setWindowTitle("E-SINAV")
        widget.show()


app = QApplication(sys.argv)
window = MainWin()
try:
    sys.exit(app.exec_())
except:
    print("exit")
