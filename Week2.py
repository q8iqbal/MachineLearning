from concept_learning import SFinder
from concept_learning import CEleminator
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    __fileName = ""

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 493)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 400, 381, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.findSButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.findSButton.setObjectName("findSButton")
        self.horizontalLayout.addWidget(self.findSButton)
        self.candidateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.candidateButton.setObjectName("candidateButton")
        self.horizontalLayout.addWidget(self.candidateButton)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 541, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 340, 521, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loadButton.setText(_translate("Dialog", "Load CSV"))
        self.findSButton.setText(_translate("Dialog", "FInd S"))
        self.candidateButton.setText(_translate("Dialog", "Candidate elemination"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.loadButton.clicked.connect(self.loadButton_handler)
        self.findSButton.clicked.connect(self.findSButton_handler)
        self.candidateButton.clicked.connect(self.candidateButton_handler)

    def loadButton_handler(self):
        _translate = QtCore.QCoreApplication.translate
        self.__fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Title", ".", "CSV (*.csv)")[0]
        self.label.setText(_translate("Dialog", "Data loaded"))
        temp = SFinder(self.__fileName)
        self.textBrowser.append("Data : \n" + str(temp.get_parsed_data()))
        self.textBrowser.append("\nTarget : " + str(temp.get_parsed_target()))

    def findSButton_handler(self):
        hip = SFinder(self.__fileName)
        self.textBrowser.setText("\nhypothesis :" + str(hip.get_result()))

    def candidateButton_handler(self):
        hip = CEleminator(self.__fileName)
        self.textBrowser.setText("\nSpecific hypothesis : " + str(hip.get_specific_hypothesis()))
        self.textBrowser.append("General hypothesis : " + str(hip.get_general_hypothesis()))
        self.textBrowser.append("Final hypothesis : " + str(hip.get_result()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
