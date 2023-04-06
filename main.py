
from random import shuffle
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from numpy import sqrt
from bagli_liste import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):

        self.puzzle=LinkedList()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1238, 846)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../puzzle/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_resim_sec = QtWidgets.QPushButton(self.centralwidget)
        self.button_resim_sec.setGeometry(QtCore.QRect(300, 30, 191, 61))
        self.button_resim_sec.setObjectName("button_resim_sec")
        self.button_resim_sec.clicked.connect(self.resimSec)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 190, 601, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_parca1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca1.sizePolicy().hasHeightForWidth())
        self.button_parca1.setSizePolicy(sizePolicy)
        self.button_parca1.setMinimumSize(QtCore.QSize(100, 100))
        self.button_parca1.setObjectName("button_parca1")
        self.gridLayout_2.addWidget(self.button_parca1, 0, 0, 1, 1)
        self.button_parca3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca3.sizePolicy().hasHeightForWidth())
        self.button_parca3.setSizePolicy(sizePolicy)
        self.button_parca3.setObjectName("button_parca3")
        self.gridLayout_2.addWidget(self.button_parca3, 0, 2, 1, 1)
        self.button_parca2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca2.sizePolicy().hasHeightForWidth())
        self.button_parca2.setSizePolicy(sizePolicy)
        self.button_parca2.setObjectName("button_parca2")
        self.gridLayout_2.addWidget(self.button_parca2, 0, 1, 1, 1)
        self.button_parca5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca5.sizePolicy().hasHeightForWidth())
        self.button_parca5.setSizePolicy(sizePolicy)
        self.button_parca5.setObjectName("button_parca5")
        self.gridLayout_2.addWidget(self.button_parca5, 1, 0, 1, 1)
        self.button_parca4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca4.sizePolicy().hasHeightForWidth())
        self.button_parca4.setSizePolicy(sizePolicy)
        self.button_parca4.setObjectName("button_parca4")
        self.gridLayout_2.addWidget(self.button_parca4, 0, 3, 1, 1)
        self.button_parca9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca9.sizePolicy().hasHeightForWidth())
        self.button_parca9.setSizePolicy(sizePolicy)
        self.button_parca9.setMinimumSize(QtCore.QSize(100, 100))
        self.button_parca9.setObjectName("button_parca9")
        self.gridLayout_2.addWidget(self.button_parca9, 2, 0, 1, 1)
        self.button_parca13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca13.sizePolicy().hasHeightForWidth())
        self.button_parca13.setSizePolicy(sizePolicy)
        self.button_parca13.setObjectName("button_parca13")
        self.gridLayout_2.addWidget(self.button_parca13, 3, 0, 1, 1)
        self.button_parca6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca6.sizePolicy().hasHeightForWidth())
        self.button_parca6.setSizePolicy(sizePolicy)
        self.button_parca6.setObjectName("button_parca6")
        self.gridLayout_2.addWidget(self.button_parca6, 1, 1, 1, 1)
        self.button_parca7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca7.sizePolicy().hasHeightForWidth())
        self.button_parca7.setSizePolicy(sizePolicy)
        self.button_parca7.setObjectName("button_parca7")
        self.gridLayout_2.addWidget(self.button_parca7, 1, 2, 1, 1)
        self.button_parca8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca8.sizePolicy().hasHeightForWidth())
        self.button_parca8.setSizePolicy(sizePolicy)
        self.button_parca8.setMinimumSize(QtCore.QSize(100, 100))
        self.button_parca8.setObjectName("button_parca8")
        self.gridLayout_2.addWidget(self.button_parca8, 1, 3, 1, 1)
        self.button_parca10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca10.sizePolicy().hasHeightForWidth())
        self.button_parca10.setSizePolicy(sizePolicy)
        self.button_parca10.setObjectName("button_parca10")
        self.gridLayout_2.addWidget(self.button_parca10, 2, 1, 1, 1)
        self.button_parca11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca11.sizePolicy().hasHeightForWidth())
        self.button_parca11.setSizePolicy(sizePolicy)
        self.button_parca11.setObjectName("button_parca11")
        self.gridLayout_2.addWidget(self.button_parca11, 2, 2, 1, 1)
        self.button_parca12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca12.sizePolicy().hasHeightForWidth())
        self.button_parca12.setSizePolicy(sizePolicy)
        self.button_parca12.setObjectName("button_parca12")
        self.gridLayout_2.addWidget(self.button_parca12, 2, 3, 1, 1)
        self.button_parca14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca14.sizePolicy().hasHeightForWidth())
        self.button_parca14.setSizePolicy(sizePolicy)
        self.button_parca14.setObjectName("button_parca14")
        self.gridLayout_2.addWidget(self.button_parca14, 3, 1, 1, 1)
        self.button_parca15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca15.sizePolicy().hasHeightForWidth())
        self.button_parca15.setSizePolicy(sizePolicy)
        self.button_parca15.setObjectName("button_parca15")
        self.gridLayout_2.addWidget(self.button_parca15, 3, 2, 1, 1)
        self.button_parca16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_parca16.sizePolicy().hasHeightForWidth())
        self.button_parca16.setSizePolicy(sizePolicy)
        self.button_parca16.setMinimumSize(QtCore.QSize(100, 100))
        self.button_parca16.setObjectName("button_parca16")
        self.gridLayout_2.addWidget(self.button_parca16, 3, 3, 1, 1)
        self.lcdNumber_skor = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_skor.setGeometry(QtCore.QRect(1100, 20, 111, 51))
        self.lcdNumber_skor.setObjectName("lcdNumber_skor")
        self.listWidget_skorlar = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_skorlar.setGeometry(QtCore.QRect(960, 200, 256, 451))
        self.listWidget_skorlar.setObjectName("listWidget_skorlar")
        self.skor_siralama()
        self.button_karistir = QtWidgets.QPushButton(self.centralwidget)
        self.button_karistir.setGeometry(QtCore.QRect(330, 670, 141, 51))
        self.button_karistir.setObjectName("button_karistir")
        self.button_karistir.clicked.connect(self.parcalari_karistir)
        self.button_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.button_cikis.setGeometry(QtCore.QRect(1104, 762, 111, 41))
        self.button_cikis.setObjectName("button_cikis")
        self.label_en_yuksek_skor = QtWidgets.QLabel(self.centralwidget)
        self.label_en_yuksek_skor.setGeometry(QtCore.QRect(1020, 170, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_en_yuksek_skor.setFont(font)
        self.label_en_yuksek_skor.setObjectName("label_en_yuksek_skor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.puzzle.ekle(self.button_parca1)
        self.puzzle.ekle(self.button_parca2)
        self.puzzle.ekle(self.button_parca3)
        self.puzzle.ekle(self.button_parca4)
        self.puzzle.ekle(self.button_parca5)
        self.puzzle.ekle(self.button_parca6)
        self.puzzle.ekle(self.button_parca7)
        self.puzzle.ekle(self.button_parca8)
        self.puzzle.ekle(self.button_parca9)
        self.puzzle.ekle(self.button_parca10)
        self.puzzle.ekle(self.button_parca11)
        self.puzzle.ekle(self.button_parca12)
        self.puzzle.ekle(self.button_parca13)
        self.puzzle.ekle(self.button_parca14)
        self.puzzle.ekle(self.button_parca15)
        self.puzzle.ekle(self.button_parca16)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Puzzle Oyunu"))
        self.button_resim_sec.setText(_translate("MainWindow", "Resim Seç"))
        self.button_parca1.setText(_translate("MainWindow", ""))
        self.button_parca3.setText(_translate("MainWindow", ""))
        self.button_parca2.setText(_translate("MainWindow", ""))
        self.button_parca5.setText(_translate("MainWindow", ""))
        self.button_parca4.setText(_translate("MainWindow", ""))
        self.button_parca9.setText(_translate("MainWindow", ""))
        self.button_parca13.setText(_translate("MainWindow", ""))
        self.button_parca6.setText(_translate("MainWindow", ""))
        self.button_parca7.setText(_translate("MainWindow", ""))
        self.button_parca8.setText(_translate("MainWindow", ""))
        self.button_parca10.setText(_translate("MainWindow", ""))
        self.button_parca11.setText(_translate("MainWindow", ""))
        self.button_parca12.setText(_translate("MainWindow", ""))
        self.button_parca14.setText(_translate("MainWindow", ""))
        self.button_parca15.setText(_translate("MainWindow", ""))
        self.button_parca16.setText(_translate("MainWindow", ""))
        self.button_karistir.setText(_translate("MainWindow", "Karıştır"))
        self.button_cikis.setText(_translate("MainWindow", "Çıkış"))
        self.label_en_yuksek_skor.setText(_translate("MainWindow", "En Yüksek Skorlar"))



    def resimSec(self):
        # Kullanıcının adını girmesini iste
        kullanici_adi, ok_pressed = QInputDialog.getText(self, "Kullanıcı Adı", " Önce Kullanıcı Adınızı Giriniz:")
        if kullanici_adi and ok_pressed:
             skor = "0" # kullanıcının puanı
             with open("enyuksekskor.txt", "a") as f:
              f.write("{} - Hamle Sayısı: {} - Puan: {}\n".format(kullanici_adi, "0", skor))

             dosyaAdi, _ = QFileDialog.getOpenFileName(self.centralwidget, "Resim Seç", "", "Resim Dosyaları (*.png *.jpg *.bmp)")
             if dosyaAdi:
                 resim = QImage(dosyaAdi)
                  # Scale the image to a new width and height
                 new_width = 601
                 new_height = 461
                 resim = resim.scaled(new_width, new_height)

                    # Display the image in a label
                 self.label_resim = QLabel(self)
                 self.label_resim.setPixmap(QPixmap.fromImage(resim))
                 self.label_resim.setGeometry(50, 50, new_width, new_height)

                 self.parcalar = []
                 self.orijinal_parcalar = []
                 sutun = satir = int(sqrt(self.puzzle.size))
                 width, height = resim.width() // sutun, resim.height() // satir
                 for i in range(sutun):
                     for j in range(satir):
                         parca = resim.copy(j*width, i*height, width, height)
                         self.parcalar.append(parca)
                         self.orijinal_parcalar.append(parca)
                 
                 for i, parca in enumerate(self.parcalar):
                   buton = getattr(self, f"button_parca{i+1}")
                   buton.setIcon(QIcon(QPixmap.fromImage(parca)))
                   buton.setIconSize(buton.size())
    
    def parcalari_karistir(self):
        while True:
            shuffle(self.parcalar)
            if any(self.parcalar[i] == self.orijinal_parcalar[i] for i in range(len(self.parcalar))):
                break

        for i, parca in enumerate(self.parcalar):
            buton = getattr(self, f"button_parca{i+1}")
            buton.setIcon(QIcon(QPixmap.fromImage(parca)))
            buton.setIconSize(buton.size())

    def skor_siralama(self):
        
        with open("enyuksekskor.txt", "r") as f:
            skorlar = f.readlines()
            skorlar = [skor.strip() for skor in skorlar]
            skorlar.sort(reverse=True)
            self.listWidget_skorlar.addItems(skorlar)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)  
    MainWindow.show()
    sys.exit(app.exec_())