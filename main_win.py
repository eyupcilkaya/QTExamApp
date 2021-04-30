import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, v):
        super(MainWindow, self).__init__()
        loadUi("ui/main.ui", self)
        self.widget = 0
        self.v = v
        self.click_method()

    def click_method(self):
        if not os.path.exists("question.xlsx"):
            self.startexam.setEnabled(False)

        self.widget = self.v.getWidget()
        self.startexam.clicked.connect(self.open_quest)
        self.loadfile.clicked.connect(self.open_load)

    def open_quest(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.v.setWidget(self.widget)

    def open_load(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 2)
        self.v.setWidget(self.widget)
