# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dizayn.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 740)
        MainWindow.setMinimumSize(QtCore.QSize(1109, 740))
        MainWindow.setMaximumSize(QtCore.QSize(1109, 740))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/address-book.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 1041, 741))
        self.stackedWidget.setStyleSheet("#page_4{\n"
"    border-image: url(:/icons/448.jpg);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("#page_1{\n"
"border-image: url(:/icons/14.jpg);\n"
"}")
        self.page_1.setObjectName("page_1")
        self.label_1 = QtWidgets.QLabel(self.page_1)
        self.label_1.setGeometry(QtCore.QRect(440, 130, 501, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.page_1)
        self.label_2.setGeometry(QtCore.QRect(660, 680, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.buton_a1 = QtWidgets.QPushButton(self.page_1)
        self.buton_a1.setGeometry(QtCore.QRect(610, 440, 161, 41))
        self.buton_a1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buton_a1.setObjectName("buton_a1")
        self.frame = QtWidgets.QFrame(self.page_1)
        self.frame.setGeometry(QtCore.QRect(470, 270, 441, 141))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(20, 1, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_hosgeldiniz = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_hosgeldiniz.setFont(font)
        self.label_hosgeldiniz.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hosgeldiniz.setObjectName("label_hosgeldiniz")
        self.verticalLayout.addWidget(self.label_hosgeldiniz)
        self.lineEdit_a1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_a1.setObjectName("lineEdit_a1")
        self.verticalLayout.addWidget(self.lineEdit_a1)
        self.labelVersion = QtWidgets.QLabel(self.page_1)
        self.labelVersion.setGeometry(QtCore.QRect(20, 680, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(11)
        font.setItalic(True)
        self.labelVersion.setFont(font)
        self.labelVersion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_b1 = QtWidgets.QLabel(self.page_2)
        self.label_b1.setGeometry(QtCore.QRect(90, 60, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_b1.setFont(font)
        self.label_b1.setObjectName("label_b1")
        self.listWidget_1 = QtWidgets.QListWidget(self.page_2)
        self.listWidget_1.setGeometry(QtCore.QRect(90, 120, 791, 421))
        self.listWidget_1.setObjectName("listWidget_1")
        self.buton_kaydet1 = QtWidgets.QPushButton(self.page_2)
        self.buton_kaydet1.setGeometry(QtCore.QRect(770, 80, 93, 28))
        self.buton_kaydet1.setObjectName("buton_kaydet1")
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 580, 631, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buton_b1 = QtWidgets.QPushButton(self.layoutWidget)
        self.buton_b1.setObjectName("buton_b1")
        self.horizontalLayout.addWidget(self.buton_b1)
        self.buton_b2 = QtWidgets.QPushButton(self.layoutWidget)
        self.buton_b2.setObjectName("buton_b2")
        self.horizontalLayout.addWidget(self.buton_b2)
        self.buton_b3 = QtWidgets.QPushButton(self.layoutWidget)
        self.buton_b3.setObjectName("buton_b3")
        self.horizontalLayout.addWidget(self.buton_b3)
        self.buton_b4 = QtWidgets.QPushButton(self.layoutWidget)
        self.buton_b4.setObjectName("buton_b4")
        self.horizontalLayout.addWidget(self.buton_b4)
        self.buton_b5 = QtWidgets.QPushButton(self.layoutWidget)
        self.buton_b5.setObjectName("buton_b5")
        self.horizontalLayout.addWidget(self.buton_b5)
        self.stackedWidget.addWidget(self.page_2)
        self.page_projects = QtWidgets.QWidget()
        self.page_projects.setObjectName("page_projects")
        self.butonEkle_pr = QtWidgets.QPushButton(self.page_projects)
        self.butonEkle_pr.setGeometry(QtCore.QRect(320, 600, 151, 28))
        self.butonEkle_pr.setObjectName("butonEkle_pr")
        self.tableWidget = QtWidgets.QTableWidget(self.page_projects)
        self.tableWidget.setGeometry(QtCore.QRect(90, 120, 791, 441))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.butonTamam = QtWidgets.QPushButton(self.page_projects)
        self.butonTamam.setGeometry(QtCore.QRect(510, 600, 141, 28))
        self.butonTamam.setObjectName("butonTamam")
        self.butonKaydet_pr = QtWidgets.QPushButton(self.page_projects)
        self.butonKaydet_pr.setGeometry(QtCore.QRect(770, 80, 91, 28))
        self.butonKaydet_pr.setObjectName("butonKaydet_pr")
        self.label_b1_2 = QtWidgets.QLabel(self.page_projects)
        self.label_b1_2.setGeometry(QtCore.QRect(100, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_b1_2.setFont(font)
        self.label_b1_2.setObjectName("label_b1_2")
        self.stackedWidget.addWidget(self.page_projects)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 570, 631, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buton_c1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.buton_c1.setObjectName("buton_c1")
        self.horizontalLayout_3.addWidget(self.buton_c1)
        self.buton_c2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.buton_c2.setObjectName("buton_c2")
        self.horizontalLayout_3.addWidget(self.buton_c2)
        self.buton_c3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.buton_c3.setObjectName("buton_c3")
        self.horizontalLayout_3.addWidget(self.buton_c3)
        self.buton_c4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.buton_c4.setObjectName("buton_c4")
        self.horizontalLayout_3.addWidget(self.buton_c4)
        self.buton_c5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.buton_c5.setObjectName("buton_c5")
        self.horizontalLayout_3.addWidget(self.buton_c5)
        self.label_c1 = QtWidgets.QLabel(self.page_3)
        self.label_c1.setGeometry(QtCore.QRect(90, 60, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_c1.setFont(font)
        self.label_c1.setObjectName("label_c1")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_3)
        self.listWidget_2.setGeometry(QtCore.QRect(90, 120, 791, 411))
        self.listWidget_2.setObjectName("listWidget_2")
        self.buton_kaydet2 = QtWidgets.QPushButton(self.page_3)
        self.buton_kaydet2.setGeometry(QtCore.QRect(770, 80, 93, 28))
        self.buton_kaydet2.setObjectName("buton_kaydet2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_profil = QtWidgets.QWidget()
        self.page_profil.setObjectName("page_profil")
        self.label = QtWidgets.QLabel(self.page_profil)
        self.label.setGeometry(QtCore.QRect(390, 60, 221, 211))
        self.label.setStyleSheet("border-image: url(:/icons/profile.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_profisim = QtWidgets.QLineEdit(self.page_profil)
        self.lineEdit_profisim.setGeometry(QtCore.QRect(310, 340, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_profisim.setFont(font)
        self.lineEdit_profisim.setObjectName("lineEdit_profisim")
        self.lineEdit_profsoyisim = QtWidgets.QLineEdit(self.page_profil)
        self.lineEdit_profsoyisim.setGeometry(QtCore.QRect(310, 430, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_profsoyisim.setFont(font)
        self.lineEdit_profsoyisim.setObjectName("lineEdit_profsoyisim")
        self.lineEdit_sifre = QtWidgets.QLineEdit(self.page_profil)
        self.lineEdit_sifre.setGeometry(QtCore.QRect(310, 520, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sifre.setFont(font)
        self.lineEdit_sifre.setObjectName("lineEdit_sifre")
        self.label_3 = QtWidgets.QLabel(self.page_profil)
        self.label_3.setGeometry(QtCore.QRect(320, 310, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_profil)
        self.label_4.setGeometry(QtCore.QRect(320, 400, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_profil)
        self.label_5.setGeometry(QtCore.QRect(320, 490, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.buton_profilKaydet = QtWidgets.QPushButton(self.page_profil)
        self.buton_profilKaydet.setGeometry(QtCore.QRect(430, 610, 141, 31))
        self.buton_profilKaydet.setObjectName("buton_profilKaydet")
        self.stackedWidget.addWidget(self.page_profil)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(55, 70))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionAna_Sayfa = QtWidgets.QAction(MainWindow)
        self.actionAna_Sayfa.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/shield.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAna_Sayfa.setIcon(icon1)
        self.actionAna_Sayfa.setObjectName("actionAna_Sayfa")
        self.actionHedefler = QtWidgets.QAction(MainWindow)
        self.actionHedefler.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionHedefler.setIcon(icon2)
        self.actionHedefler.setObjectName("actionHedefler")
        self.actionBitirilen = QtWidgets.QAction(MainWindow)
        self.actionBitirilen.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionBitirilen.setIcon(icon3)
        self.actionBitirilen.setObjectName("actionBitirilen")
        self.actionProjeler = QtWidgets.QAction(MainWindow)
        self.actionProjeler.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/projects.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionProjeler.setIcon(icon4)
        self.actionProjeler.setObjectName("actionProjeler")
        self.actionProfilim = QtWidgets.QAction(MainWindow)
        self.actionProfilim.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProfilim.setIcon(icon5)
        self.actionProfilim.setObjectName("actionProfilim")
        self.toolBar.addAction(self.actionAna_Sayfa)
        self.toolBar.addAction(self.actionHedefler)
        self.toolBar.addAction(self.actionProjeler)
        self.toolBar.addAction(self.actionBitirilen)
        self.toolBar.addAction(self.actionProfilim)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Planlama Sistemim"))
        self.label_1.setText(_translate("MainWindow", "Planlama Hedefleri Kay??t Sistemim"))
        self.label_2.setText(_translate("MainWindow", "Designed by Mehmet KAHRAMAN 2020"))
        self.buton_a1.setText(_translate("MainWindow", "Tamam"))
        self.label_hosgeldiniz.setText(_translate("MainWindow", "Ho??geldiniz, L??tfen ??ifrenizi girin."))
        self.labelVersion.setText(_translate("MainWindow", "version"))
        self.label_b1.setText(_translate("MainWindow", "Hedefteki Kategoriler:"))
        self.buton_kaydet1.setText(_translate("MainWindow", "Kaydet"))
        self.buton_b1.setText(_translate("MainWindow", "Yeni Ekle"))
        self.buton_b2.setText(_translate("MainWindow", "Se??ileni Sil"))
        self.buton_b3.setText(_translate("MainWindow", "A??a???? Ta????"))
        self.buton_b4.setText(_translate("MainWindow", "Yukar?? Ta????"))
        self.buton_b5.setText(_translate("MainWindow", "Se??ileni D??zenle"))
        self.butonEkle_pr.setText(_translate("MainWindow", "Yeni Ekle"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A????klama"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Alan"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tarih"))
        self.butonTamam.setText(_translate("MainWindow", "Tamamland??"))
        self.butonKaydet_pr.setText(_translate("MainWindow", "Kaydet"))
        self.label_b1_2.setText(_translate("MainWindow", "Projelerim:"))
        self.buton_c1.setText(_translate("MainWindow", "Yeni Ekle"))
        self.buton_c2.setText(_translate("MainWindow", "Se??ileni Sil"))
        self.buton_c3.setText(_translate("MainWindow", "A??a???? Ta????"))
        self.buton_c4.setText(_translate("MainWindow", "Yukar?? Ta????"))
        self.buton_c5.setText(_translate("MainWindow", "Se??ileni D??zenle"))
        self.label_c1.setText(_translate("MainWindow", "Tamamlanan Becerilerim:"))
        self.buton_kaydet2.setText(_translate("MainWindow", "Kaydet"))
        self.label_3.setText(_translate("MainWindow", "??sim:"))
        self.label_4.setText(_translate("MainWindow", "Soyisim:"))
        self.label_5.setText(_translate("MainWindow", "??ifre:"))
        self.buton_profilKaydet.setText(_translate("MainWindow", "KAYDET"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAna_Sayfa.setText(_translate("MainWindow", "Ana Sayfa"))
        self.actionHedefler.setText(_translate("MainWindow", "Hedefler"))
        self.actionBitirilen.setText(_translate("MainWindow", "Bitirilen"))
        self.actionProjeler.setText(_translate("MainWindow", "Projeler"))
        self.actionProfilim.setText(_translate("MainWindow", "Profilim"))
import icons_rc
