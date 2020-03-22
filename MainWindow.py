# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setEnabled(True)
        Main.resize(1558, 723)
        Main.setMouseTracking(False)
        Main.setAutoFillBackground(False)
        Main.setStyleSheet("background-color: #3a3a47;")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.tw_show = QtWidgets.QTableWidget(self.centralwidget)
        self.tw_show.setGeometry(QtCore.QRect(24, 12, 1519, 613))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tw_show.setFont(font)
        self.tw_show.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_show.setTabKeyNavigation(True)
        self.tw_show.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_show.setRowCount(50)
        self.tw_show.setColumnCount(7)
        self.tw_show.setObjectName("tw_show")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tw_show.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_show.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_show.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_show.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_show.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_show.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_show.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_show.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_show.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_show.setItem(0, 2, item)
        self.tw_show.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_show.horizontalHeader().setDefaultSectionSize(211)
        self.tw_show.horizontalHeader().setSortIndicatorShown(False)
        self.tw_show.horizontalHeader().setStretchLastSection(True)
        self.tw_show.verticalHeader().setDefaultSectionSize(29)
        self.tw_show.verticalHeader().setMinimumSectionSize(27)
        self.tw_show.verticalHeader().setStretchLastSection(True)
        self.cb_show = QtWidgets.QComboBox(self.centralwidget)
        self.cb_show.setGeometry(QtCore.QRect(60, 654, 229, 31))
        self.cb_show.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_show.setFont(font)
        self.cb_show.setStyleSheet("color: #FFF;")
        self.cb_show.setObjectName("cb_show")
        self.cb_show.addItem("")
        self.cb_show.addItem("")
        self.cb_show.addItem("")
        self.cb_show.addItem("")
        self.cb_show.addItem("")
        self.cb_show.addItem("")
        self.lbl_addingWorker = QtWidgets.QPushButton(self.centralwidget)
        self.lbl_addingWorker.setGeometry(QtCore.QRect(1308, 636, 193, 28))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbl_addingWorker.setFont(font)
        self.lbl_addingWorker.setStyleSheet("QPushButton{\n"
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
        self.lbl_addingWorker.setObjectName("lbl_addingWorker")
        self.lbl_show = QtWidgets.QPushButton(self.centralwidget)
        self.lbl_show.setGeometry(QtCore.QRect(306, 654, 133, 28))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbl_show.setFont(font)
        self.lbl_show.setStyleSheet("QPushButton{\n"
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
        self.lbl_show.setObjectName("lbl_show")
        self.lbl_updating = QtWidgets.QPushButton(self.centralwidget)
        self.lbl_updating.setGeometry(QtCore.QRect(1074, 654, 193, 28))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbl_updating.setFont(font)
        self.lbl_updating.setStyleSheet("QPushButton{\n"
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
        self.lbl_updating.setObjectName("lbl_updating")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(468, 648, 289, 37))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.hl_id = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hl_id.setContentsMargins(0, 0, 0, 0)
        self.hl_id.setObjectName("hl_id")
        self.lbl_id = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_id.setFont(font)
        self.lbl_id.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_id.setObjectName("lbl_id")
        self.hl_id.addWidget(self.lbl_id)
        self.le_id = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_id.setFont(font)
        self.le_id.setStyleSheet("color: rgb(255, 255, 255);")
        self.le_id.setObjectName("le_id")
        self.hl_id.addWidget(self.le_id)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(768, 648, 289, 37))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.hl_id_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.hl_id_2.setContentsMargins(0, 0, 0, 0)
        self.hl_id_2.setObjectName("hl_id_2")
        self.lbl_id_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_id_2.setFont(font)
        self.lbl_id_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_id_2.setObjectName("lbl_id_2")
        self.hl_id_2.addWidget(self.lbl_id_2)
        self.le_id_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_id_2.setFont(font)
        self.le_id_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.le_id_2.setObjectName("le_id_2")
        self.hl_id_2.addWidget(self.le_id_2)
        self.lbl_addingWorker_2 = QtWidgets.QPushButton(self.centralwidget)
        self.lbl_addingWorker_2.setGeometry(QtCore.QRect(1308, 672, 193, 28))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbl_addingWorker_2.setFont(font)
        self.lbl_addingWorker_2.setStyleSheet("QPushButton{\n"
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
        self.lbl_addingWorker_2.setObjectName("lbl_addingWorker_2")
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        item = self.tw_show.horizontalHeaderItem(0)
        item.setText(_translate("Main", "Name"))
        item = self.tw_show.horizontalHeaderItem(1)
        item.setText(_translate("Main", "Type"))
        item = self.tw_show.horizontalHeaderItem(2)
        item.setText(_translate("Main", "Id"))
        item = self.tw_show.horizontalHeaderItem(3)
        item.setText(_translate("Main", "Birthday"))
        item = self.tw_show.horizontalHeaderItem(4)
        item.setText(_translate("Main", "First day"))
        item = self.tw_show.horizontalHeaderItem(5)
        item.setText(_translate("Main", "Salary(basic+bonus)"))
        item = self.tw_show.horizontalHeaderItem(6)
        item.setText(_translate("Main", "password"))
        __sortingEnabled = self.tw_show.isSortingEnabled()
        self.tw_show.setSortingEnabled(False)
        self.tw_show.setSortingEnabled(__sortingEnabled)
        self.cb_show.setItemText(0, _translate("Main", "Everyone"))
        self.cb_show.setItemText(1, _translate("Main", "Type"))
        self.cb_show.setItemText(2, _translate("Main", "Salary"))
        self.cb_show.setItemText(3, _translate("Main", "Bonus"))
        self.cb_show.setItemText(4, _translate("Main", "Age"))
        self.cb_show.setItemText(5, _translate("Main", "Time worked"))
        self.lbl_addingWorker.setText(_translate("Main", "Add worker"))
        self.lbl_show.setText(_translate("Main", "Show"))
        self.lbl_updating.setText(_translate("Main", "Update"))
        self.lbl_id.setText(_translate("Main", "Basic salary:"))
        self.lbl_id_2.setText(_translate("Main", "Bonus per hour/buyer:"))
        self.lbl_addingWorker_2.setText(_translate("Main", "Delete worker"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
