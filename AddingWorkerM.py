# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddingWorkerM.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addingWorker(object):
    def setupUi(self, addingWorker):
        addingWorker.setObjectName("addingWorker")
        addingWorker.resize(271, 193)
        addingWorker.setStyleSheet("background-color: #3a3a47;")
        self.centralwidget = QtWidgets.QWidget(addingWorker)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(24, 30, 217, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setWhatsThis("")
        self.lbl_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(558, 666, 163, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("QPushButton{\n"
"  background-color: rgb(255, 171, 2);\n"
"  border: none;\n"
"  color: white;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  cursor: pointer;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 137, 2);\n"
"    color: rgb(217, 217, 217);\n"
"}")
        self.btn_add.setAutoDefault(False)
        self.btn_add.setDefault(False)
        self.btn_add.setFlat(False)
        self.btn_add.setObjectName("btn_add")
        self.cb_type = QtWidgets.QComboBox(self.centralwidget)
        self.cb_type.setGeometry(QtCore.QRect(36, 84, 199, 31))
        self.cb_type.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_type.setFont(font)
        self.cb_type.setStyleSheet("color: #FFF;")
        self.cb_type.setObjectName("cb_type")
        self.cb_type.addItem("")
        self.lbl_add = QtWidgets.QPushButton(self.centralwidget)
        self.lbl_add.setGeometry(QtCore.QRect(66, 132, 133, 28))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbl_add.setFont(font)
        self.lbl_add.setStyleSheet("QPushButton{\n"
"  background-color: rgb(255, 171, 2);\n"
"  border: none;\n"
"  color: white;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  cursor: pointer;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 137, 2);\n"
"    color: rgb(217, 217, 217);\n"
"}")
        self.lbl_add.setObjectName("lbl_add")
        addingWorker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addingWorker)
        self.statusbar.setObjectName("statusbar")
        addingWorker.setStatusBar(self.statusbar)

        self.retranslateUi(addingWorker)
        QtCore.QMetaObject.connectSlotsByName(addingWorker)

    def retranslateUi(self, addingWorker):
        _translate = QtCore.QCoreApplication.translate
        addingWorker.setWindowTitle(_translate("addingWorker", "Adding worker"))
        self.lbl_title.setText(_translate("addingWorker", "Last step:"))
        self.btn_add.setText(_translate("addingWorker", "add/change"))
        self.cb_type.setItemText(0, _translate("addingWorker", "Choose maneger"))
        self.lbl_add.setText(_translate("addingWorker", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addingWorker = QtWidgets.QMainWindow()
    ui = Ui_addingWorker()
    ui.setupUi(addingWorker)
    addingWorker.show()
    sys.exit(app.exec_())
