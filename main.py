import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication
import variables
import main_win
import load_win
import question_win
import info_win

v = variables.variables()


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        loadUi("ui/main.ui", self)
        v.setWidget(widget)
        main_win.MainWindow.click_method(self, v)


class LoadWin(QFrame):
    def __init__(self):
        super(LoadWin, self).__init__()
        loadUi("ui/load.ui", self)
        load_win.LoadWindow.click_method(self, v)


class QuestWin(QFrame):
    def __init__(self):
        super(QuestWin, self).__init__()
        loadUi("ui/question.ui", self)
        question_win.QuestionWindow.clicked_method(self, v)


class InfoWin(QFrame):
    def __init__(self):
        super(InfoWin, self).__init__()
        loadUi("ui/info.ui", self)
        info_win.InfoWindow.clicked_method(self, v)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainWindow = MainWin()
questWindow = QuestWin()
loadWindow = LoadWin()
infoWindow = InfoWin()
widget.addWidget(mainWindow)
widget.addWidget(questWindow)
widget.addWidget(loadWindow)
widget.addWidget(infoWindow)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.setWindowTitle("E-SINAV")
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exit")
