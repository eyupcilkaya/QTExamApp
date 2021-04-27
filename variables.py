class variables():
    def __init__(self):
        self.ta = 0
        self.fa = 0
        self.ea = 0
        self.widget = 0

    def setAnswer(self, t, f, e):
        self.ta = t
        self.fa = f
        self.ea = e

    def getAnswer(self):
        return self.ta, self.fa, self.ea

    def setWidget(self, widget):
        self.widget = widget

    def getWidget(self):
        return self.widget
