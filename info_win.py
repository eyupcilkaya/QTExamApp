from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class InfoWindow(QtWidgets.QFrame):
    def __init__(self, v):
        super(InfoWindow, self).__init__()
        loadUi("ui/info.ui", self)
        self.widget = 0
        self.v = v
        self.clicked_method()

    def clicked_method(self):
        self.widget = self.v.getWidget()
        self.finish.clicked.connect(self.print_result)
        self.cancel.clicked.connect(self.give_up)

    def print_result(self):
        self.widget = self.v.getWidget()
        variables = self.v.getAnswer()
        self.info.setText(f"Doğru Cevap Sayısı : {variables[0]} \n"
                          f"Yanlış Cevap Sayısı : {variables[1]} \n"
                          f"Boş Cevap Sayısı : {variables[2]}")
        self.finish.setVisible(False)
        self.cancel.setText("KAPAT")

        self.cancel.clicked.connect(lambda: self.widget.close())

    def give_up(self):
        self.widget = self.v.getWidget()
        self.widget.setFixedWidth(800)
        self.widget.setFixedHeight(600)
        self.widget.setCurrentIndex(self.widget.currentIndex() - 2)
