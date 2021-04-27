import os


class MainWindow():
    def __init__(self):
        self.widget = 0

    def click_method(self, v):
        if (not os.path.exists("question.xlsx")):
            self.startexam.setEnabled(False)
        self.v = v
        self.widget = self.v.getWidget()
        self.startexam.clicked.connect(lambda: MainWindow.open_quest(self))
        self.loadfile.clicked.connect(lambda: MainWindow.open_load(self))

    def open_quest(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.v.setWidget(self.widget)

    def open_load(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 2)
        self.v.setWidget(self.widget)
