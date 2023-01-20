from mhyt import yt_download
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 353)
        MainWindow.setStyleSheet("background-color: rgb(33, 45, 86);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(424, 240, 101, 31))
        self.bt_download.setStyleSheet("QPushButton{\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    border: 2px solid  white;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    border: 2px solid  black;\n"
                                       "}\n"
                                       "")
        self.bt_download.setObjectName("bt_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 160, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 47, 13))
        self.label_2.setObjectName("label_2")
        self.inp_link = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_link.setGeometry(QtCore.QRect(100, 150, 431, 31))
        self.inp_link.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_link.setObjectName("inp_link")
        self.inp_title = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_title.setGeometry(QtCore.QRect(100, 190, 431, 31))
        self.inp_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_title.setObjectName("inp_title")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 101, 71))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 230, 45, 42))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_mp3 = QtWidgets.QRadioButton(self.widget)
        self.rb_mp3.setStyleSheet("color: rgb(255, 255, 255);")
        self.rb_mp3.setChecked(True)
        self.rb_mp3.setObjectName("rb_mp3")
        self.verticalLayout.addWidget(self.rb_mp3)
        self.rb_mp4 = QtWidgets.QRadioButton(self.widget)
        self.rb_mp4.setStyleSheet("color: rgb(255, 255, 255);")
        self.rb_mp4.setObjectName("rb_mp4")
        self.verticalLayout.addWidget(self.rb_mp4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## BOtão Download
        self.bt_download.clicked.connect(self.download)

    def download(self):
        url = self.inp_link.text()
        if self.rb_mp4.isChecked():
            titulo = self.inp_title.text() + ".mp4"
            yt_download(url, titulo, False)
        else:
            try:
                titulo = self.inp_title.text() + ".mp3"
                yt_download(url, titulo, ismusic=True, codec='mp3')
            except:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#ffffff;\">Link:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Titulo</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Download Videos do YouTube"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><img src=\":/youtubeImg/CDELOOPER.png\"/></p></body></html>"))
        self.rb_mp3.setText(_translate("MainWindow", "mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "mp4"))

import youtube
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
