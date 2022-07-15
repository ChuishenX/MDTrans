from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import QPushButton, QSizePolicy, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(210, 168)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.transform = QPushButton(self.centralwidget)
        self.transform.setObjectName(u"transform")
        self.transform.setGeometry(QRect(10, 90, 191, 32))
        self.mdopener = QPushButton(self.centralwidget)
        self.mdopener.setObjectName(u"mdopener")
        self.mdopener.setGeometry(QRect(10, 10, 191, 32))
        self.trword = QPushButton(self.centralwidget)
        self.trword.setObjectName(u"trword")
        self.trword.setGeometry(QRect(10, 50, 191, 32))
        self.trpdf = QPushButton(self.centralwidget)
        self.trpdf.setObjectName(u"trpdf")
        self.trpdf.setGeometry(QRect(10, 130, 191, 32))
        sizePolicy.setHeightForWidth(self.trpdf.sizePolicy().hasHeightForWidth())
        self.trpdf.setSizePolicy(sizePolicy)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Markdown\u8f6c\u6362", None))
        self.transform.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5316\u4e3aHTML", None))
        self.mdopener.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00MD\u6587\u4ef6", None))
        self.trword.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5316\u4e3aWord", None))
        self.trpdf.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5316\u4e3aPDF", None))