import shutil
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets


class LoadWindow(QtWidgets.QFrame):
    def __init__(self, v):
        super(LoadWindow, self).__init__()
        loadUi("ui/load.ui", self)
        self.widget = 0
        self.v = v
        self.click_method()

    def click_method(self):
        self.widget = self.v.getWidget()
        self.load.clicked.connect(self.load_files)

    def load_files(self):
        if self.password.text() == "123456":
            try:
                xlsx = self.excelfile.text()
                images = self.imagefile.text()
                shutil.copyfile(xlsx, "question.xlsx")
                shutil.copytree(images, "resim")
                self.info.setText("İşlem başarılı soruların yüklenmesi için yeniden başlatın.")
            except:
                self.info.setText("Dosya yolları yanlış lütfen kontrol edin.")
        else:
            self.info.setText("Şifre hatalı")
