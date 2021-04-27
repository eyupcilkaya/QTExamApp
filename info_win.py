from PyQt5 import QtWidgets


class InfoWindow(QtWidgets.QFrame):
    def __init__(self):
        self.widget = 0

    def clicked_method(self, v):
        self.v = v
        self.widget = self.v.getWidget()
        self.finish.clicked.connect(lambda: InfoWindow.print_result(self))
        self.cancel.clicked.connect(lambda: InfoWindow.give_up(self))

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
