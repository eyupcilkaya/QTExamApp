import shutil


class LoadWindow():
    def __init__(self):
        self.widget = 0

    def click_method(self, v):
        self.widget = v.getWidget()
        self.load.clicked.connect(lambda: LoadWindow.load_files(self))

    def load_files(self):
        if (self.password.text() == "123456"):
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
