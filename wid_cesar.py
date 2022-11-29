# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wid_cesar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cryptageclasse as cc
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(422, 332)
        Form.setMinimumSize(QtCore.QSize(422, 332))
        Form.setMaximumSize(QtCore.QSize(422, 332))
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(90, 20, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova Cond")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label1.setObjectName("label1")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 381, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(11)
        self.label2.setFont(font)
        self.label2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label2.setObjectName("label2")
        self.horizontalLayout.addWidget(self.label2)
        self.ModeInput = QtWidgets.QComboBox(self.layoutWidget)
        self.ModeInput.setMinimumSize(QtCore.QSize(200, 30))
        self.ModeInput.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.ModeInput.setFont(font)
        self.ModeInput.setEditable(False)
        self.ModeInput.setObjectName("ModeInput")
        self.ModeInput.addItem("")
        self.ModeInput.addItem("")
        self.horizontalLayout.addWidget(self.ModeInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(11)
        self.label3.setFont(font)
        self.label3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label3.setObjectName("label3")
        self.horizontalLayout_2.addWidget(self.label3)
        self.TextInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.TextInput.setMinimumSize(QtCore.QSize(200, 30))
        self.TextInput.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.TextInput.setFont(font)
        self.TextInput.setObjectName("TextInput")
        self.horizontalLayout_2.addWidget(self.TextInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(11)
        self.label4.setFont(font)
        self.label4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label4.setObjectName("label4")
        self.horizontalLayout_3.addWidget(self.label4)
        self.KeyInput = QtWidgets.QSpinBox(self.layoutWidget)
        self.KeyInput.setMinimumSize(QtCore.QSize(50, 30))
        self.KeyInput.setMaximumSize(QtCore.QSize(50, 30))
        self.KeyInput.setMaximum(999999999)
        self.KeyInput.setObjectName("KeyInput")
        self.horizontalLayout_3.addWidget(self.KeyInput)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(11)
        self.label5.setFont(font)
        self.label5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label5.setObjectName("label5")
        self.horizontalLayout_4.addWidget(self.label5)
        self.TextOutput = QtWidgets.QLabel(self.layoutWidget)
        self.TextOutput.setMinimumSize(QtCore.QSize(200, 30))
        self.TextOutput.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(10)
        self.TextOutput.setFont(font)
        self.TextOutput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.TextOutput.setText("")
        self.TextOutput.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.TextOutput.setObjectName("TextOutput")
        self.horizontalLayout_4.addWidget(self.TextOutput)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 280, 381, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ClearButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.ClearButton.setMinimumSize(QtCore.QSize(110, 30))
        self.ClearButton.setMaximumSize(QtCore.QSize(110, 30))
        self.ClearButton.setObjectName("ClearButton")
        self.horizontalLayout_5.addWidget(self.ClearButton)
        self.CopyButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.CopyButton.setMinimumSize(QtCore.QSize(110, 30))
        self.CopyButton.setMaximumSize(QtCore.QSize(110, 30))
        self.CopyButton.setObjectName("CopyButton")
        self.horizontalLayout_5.addWidget(self.CopyButton)
        self.OKButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.OKButton.setMinimumSize(QtCore.QSize(110, 30))
        self.OKButton.setMaximumSize(QtCore.QSize(110, 30))
        self.OKButton.setObjectName("OKButton")
        self.horizontalLayout_5.addWidget(self.OKButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cryptage César"))
        self.label1.setText(_translate("Form", "Cryptage César"))
        self.label2.setText(_translate("Form", "Mode :"))
        self.ModeInput.setCurrentText(_translate("Form", "Cryptage"))
        self.ModeInput.setItemText(0, _translate("Form", "Cryptage"))
        self.ModeInput.setItemText(1, _translate("Form", "Décryptage"))
        self.label3.setText(_translate("Form", "Texte entrée :"))
        self.label4.setText(_translate("Form", "Clé de cryptage :"))
        self.label5.setText(_translate("Form", "Texte sortie :"))
        self.ClearButton.setText(_translate("Form", "CLEAR"))
        self.CopyButton.setText(_translate("Form", "COPIE SORTIE"))
        self.OKButton.setText(_translate("Form", "OK"))


    def clear(self):
        """remet tout à 0 quand le bouton clear est pressé"""
        self.TextInput.setText('')
        self.TextOutput.setText("")
        self.KeyInput.setValue(0)
        self.ModeInput.setCurrentIndex(0)

    def cryptage(self, mode=None):
        """crypte en cesar a partir de cryptageclasse.py"""
        try:        
            msg=cc.Message(str(self.TextInput.text()))
            if self.ModeInput.currentIndex()==0:            #mode cryptage
                msg.modecryptage(True)
            else:
                msg.modecryptage(False)
            cle=cc.Clé(str(self.KeyInput.text()))
            msg.cesar(cle)
            self.TextOutput.setText(str(msg.texte))
        except Exception:
            self.clear()
            self.TextInput.setText("### ERROR ###")
            self.TextOutput.setText(str(Exception))

    def copie(self): #il faut rajouter un bouton de copie sur le widget
        """copie le texte de sortie dans le presse papier"""
        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.setText(self.TextOutput.text())

def main_cesar():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.ClearButton.clicked.connect(lambda : ui.clear()) #bouton clear
    ui.OKButton.clicked.connect(lambda: ui.cryptage()) #bouton ok
    ui.CopyButton.clicked.connect(lambda : ui.copie()) #bouton copie
    sys.exit(app.exec_())

if __name__ == "__main__":
    main_cesar()
