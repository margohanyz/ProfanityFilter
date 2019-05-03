from PyQt4 import QtCore, QtGui
import Scraping as sc
#import os

#url = 'https://twitter.com/realdonaldtrump'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.width = 1500
        self.height = 800
        MainWindow.setObjectName(_fromUtf8("Profanity Filter"))
        MainWindow.resize(self.width, self.height)
        MainWindow.move(0,0)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # Button
        self.GObutton = QtGui.QPushButton(self.centralwidget)
        self.GObutton.setGeometry(QtCore.QRect(725, 20, 200, 45))
        self.GObutton.setObjectName(_fromUtf8("GObutton"))
        ###### EVENT ##########
        self.GObutton.clicked.connect(self.GOclick)
        self.GObutton.setStyleSheet(_fromUtf8("QPushButton {\n"
                                                "background: rgb(255, 255, 255)\n"
                                                "}"))

        # URL
        self.URlline = QtGui.QLineEdit(self.centralwidget)
        self.URlline.setGeometry(QtCore.QRect(20, 20, 700, 20))
        self.URlline.setObjectName(_fromUtf8("URLline"))
        self.URlline.setStyleSheet(_fromUtf8("QLineEdit {\n"
                                                "background: rgb(255, 255, 255)\n"
                                                "}"))

        # WORD
        self.WORDline = QtGui.QLineEdit(self.centralwidget)
        self.WORDline.setGeometry(QtCore.QRect(20, 45, 700, 20))
        self.WORDline.setObjectName(_fromUtf8("WORDline"))
        self.WORDline.setStyleSheet(_fromUtf8("QLineEdit {\n"
                                             "background: rgb(255, 255, 255)\n"
                                             "}"))

        # WebSite
        self.Website = QtWebKit.QWebView(self.centralwidget)
        self.Website.setGeometry(QtCore.QRect(20, 70, (self.width-40), (self.height-85)))
        #self.Website.setUrl(QtCore.QUrl(_fromUtf8("http://www.google.com")))
        self.Website.setObjectName(_fromUtf8("WebSite"))
        self.Website.setStyleSheet(_fromUtf8("QWebView {\n"
                                              "background: rgb(255, 255, 255)\n"
                                              "}"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Profanity Filter", None))
        self.GObutton.setText(_translate("MainWindow", "GO", None))
        self.URlline.setText(_translate("MainWindow", "Please Enter A Valid URL", None))
        self.WORDline.setText(_translate("MainWindow", "Please Enter A Valid Word", None))

    def GOclick(self):
        path = self.URlline.text()
        word = self.WORDline.text()
        self.Website.setUrl(QtCore.QUrl("https://twitter.com/realdonaldtrump"))
        #elf.Website.setHtml(sc.tweet_scroller(path,word))
        #self.Website.load(QtCore.QUrl().fromLocalFile(
        #    os.path.split(os.path.abspath(__file__))[0] + r'\sourcepage.html'
        #))

        MainWindow.update()
        #self.update()
        print("Button clicked")

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

