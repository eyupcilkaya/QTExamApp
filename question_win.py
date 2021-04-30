import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import numpy as np


class QuestionWindow(QtWidgets.QFrame):
    def __init__(self, v):
        super(QuestionWindow, self).__init__()
        loadUi("ui/question.ui", self)
        self.i = 0
        self.widget = 0
        self.v = v
        self.clicked_method()

    def clicked_method(self):
        self.widget = self.v.getWidget()

        try:
            self.df = pd.read_excel('question.xlsx')
            self.answers = np.empty(len(self.df), dtype=str)
            self.next_question()
        except:
            print("soru yok")

        self.next.clicked.connect(self.next_question)
        self.back.clicked.connect(self.back_question)
        self.finish.clicked.connect(self.finished)
        self.option_a.clicked.connect(lambda: self.save("a"))
        self.option_b.clicked.connect(lambda: self.save("b"))
        self.option_c.clicked.connect(lambda: self.save("c"))
        self.option_d.clicked.connect(lambda: self.save("d"))
        self.option_e.clicked.connect(lambda: self.save("e"))

    def save(self, answer):
        self.answers[self.i - 1] = answer

    def next_question(self):

        if self.i < len(self.df):
            self.question.setText(self.df['soru'][self.i])
            self.option_a.setText(self.df['a'][self.i])
            self.option_b.setText(self.df['b'][self.i])
            self.option_c.setText(self.df['c'][self.i])
            self.option_d.setText(self.df['d'][self.i])
            self.option_e.setText(self.df['e'][self.i])
            self.frame.setStyleSheet('background-image : url({})'.format("resim/" + self.df['resim'][self.i]))
            self.i += 1
            self.mark()

    def back_question(self):
        if self.i > 1:
            self.i -= 2
            self.question.setText(self.df['soru'][self.i])
            self.option_a.setText(self.df['a'][self.i])
            self.option_b.setText(self.df['b'][self.i])
            self.option_c.setText(self.df['c'][self.i])
            self.option_d.setText(self.df['d'][self.i])
            self.option_e.setText(self.df['e'][self.i])
            self.frame.setStyleSheet('background-image : url({})'.format("resim/" + self.df['resim'][self.i]))
            self.i += 1
        self.mark()

    def finished(self):
        self.results()
        self.widget = self.v.getWidget()
        self.widget.setFixedWidth(330)
        self.widget.setFixedHeight(250)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 2)

    def mark(self):
        i = self.i - 1
        if self.answers[i] == "a":
            self.option_a.setChecked(True)
        elif self.answers[i] == "b":
            self.option_b.setChecked(True)
        elif self.answers[i] == "c":
            self.option_c.setChecked(True)
        elif self.answers[i] == "d":
            self.option_d.setChecked(True)
        elif self.answers[i] == "e":
            self.option_e.setChecked(True)
        else:
            self.clear()

    def clear(self):
        self.option_a.setAutoExclusive(False)
        self.option_b.setAutoExclusive(False)
        self.option_c.setAutoExclusive(False)
        self.option_d.setAutoExclusive(False)
        self.option_e.setAutoExclusive(False)
        self.option_a.setChecked(False)
        self.option_b.setChecked(False)
        self.option_c.setChecked(False)
        self.option_d.setChecked(False)
        self.option_e.setChecked(False)
        self.option_a.setAutoExclusive(True)
        self.option_b.setAutoExclusive(True)
        self.option_c.setAutoExclusive(True)
        self.option_d.setAutoExclusive(True)
        self.option_e.setAutoExclusive(True)

    def results(self):
        trueAnswer = 0
        falseAnswer = 0
        emptyAnswer = 0

        for i in range(len(self.df)):
            if self.answers[i] == '':
                emptyAnswer = emptyAnswer + 1
            elif self.df["cevap"][i] == self.answers[i]:
                trueAnswer = trueAnswer + 1
            else:
                falseAnswer = falseAnswer + 1
        self.v.setAnswer(trueAnswer, falseAnswer, emptyAnswer)