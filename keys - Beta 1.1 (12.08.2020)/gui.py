# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 683)
        MainWindow.setStyleSheet("background-color: #303030; \n"
"color: #ffa550;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 300, 761, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.p2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.p2.setFont(font)
        self.p2.setStyleSheet("")
        self.p2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2.setObjectName("p2")
        self.gridLayout.addWidget(self.p2, 1, 1, 1, 1)
        self.p3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.p3.setFont(font)
        self.p3.setStyleSheet("")
        self.p3.setAlignment(QtCore.Qt.AlignCenter)
        self.p3.setObjectName("p3")
        self.gridLayout.addWidget(self.p3, 1, 2, 1, 1)
        self.p1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.p1.setFont(font)
        self.p1.setStyleSheet("")
        self.p1.setAlignment(QtCore.Qt.AlignCenter)
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 1, 0, 1, 1)
        self.p5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.p5.setFont(font)
        self.p5.setStyleSheet("")
        self.p5.setAlignment(QtCore.Qt.AlignCenter)
        self.p5.setObjectName("p5")
        self.gridLayout.addWidget(self.p5, 1, 4, 1, 1)
        self.p4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.p4.setFont(font)
        self.p4.setStyleSheet("")
        self.p4.setAlignment(QtCore.Qt.AlignCenter)
        self.p4.setObjectName("p4")
        self.gridLayout.addWidget(self.p4, 1, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 440, 761, 83))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.e1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.e1.setObjectName("e1")
        self.gridLayout_3.addWidget(self.e1, 0, 0, 1, 1)
        self.i1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.i1.setObjectName("i1")
        self.gridLayout_3.addWidget(self.i1, 1, 0, 1, 1)
        self.e2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.e2.setObjectName("e2")
        self.gridLayout_3.addWidget(self.e2, 0, 1, 1, 1)
        self.e4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.e4.setObjectName("e4")
        self.gridLayout_3.addWidget(self.e4, 0, 3, 1, 1)
        self.e3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.e3.setObjectName("e3")
        self.gridLayout_3.addWidget(self.e3, 0, 2, 1, 1)
        self.e5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.e5.setObjectName("e5")
        self.gridLayout_3.addWidget(self.e5, 0, 4, 1, 1)
        self.i2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.i2.setObjectName("i2")
        self.gridLayout_3.addWidget(self.i2, 1, 1, 1, 1)
        self.i3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.i3.setObjectName("i3")
        self.gridLayout_3.addWidget(self.i3, 1, 2, 1, 1)
        self.i4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.i4.setObjectName("i4")
        self.gridLayout_3.addWidget(self.i4, 1, 3, 1, 1)
        self.i5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.i5.setObjectName("i5")
        self.gridLayout_3.addWidget(self.i5, 1, 4, 1, 1)
        self.edit_lbl = QtWidgets.QLabel(self.centralwidget)
        self.edit_lbl.setGeometry(QtCore.QRect(10, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.edit_lbl.setFont(font)
        self.edit_lbl.setStyleSheet("")
        self.edit_lbl.setObjectName("edit_lbl")
        self.edit_num = QtWidgets.QLabel(self.centralwidget)
        self.edit_num.setGeometry(QtCore.QRect(120, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.edit_num.setFont(font)
        self.edit_num.setStyleSheet("")
        self.edit_num.setObjectName("edit_num")
        self.lvl_lbl = QtWidgets.QLabel(self.centralwidget)
        self.lvl_lbl.setGeometry(QtCore.QRect(10, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.lvl_lbl.setFont(font)
        self.lvl_lbl.setStyleSheet("")
        self.lvl_lbl.setObjectName("lvl_lbl")
        self.lvl_num = QtWidgets.QLabel(self.centralwidget)
        self.lvl_num.setGeometry(QtCore.QRect(110, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.lvl_num.setFont(font)
        self.lvl_num.setStyleSheet("")
        self.lvl_num.setObjectName("lvl_num")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 761, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.r1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.r1.setFont(font)
        self.r1.setStyleSheet("")
        self.r1.setAlignment(QtCore.Qt.AlignCenter)
        self.r1.setObjectName("r1")
        self.horizontalLayout.addWidget(self.r1)
        self.r2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.r2.setFont(font)
        self.r2.setStyleSheet("")
        self.r2.setAlignment(QtCore.Qt.AlignCenter)
        self.r2.setObjectName("r2")
        self.horizontalLayout.addWidget(self.r2)
        self.r3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.r3.setFont(font)
        self.r3.setStyleSheet("")
        self.r3.setAlignment(QtCore.Qt.AlignCenter)
        self.r3.setObjectName("r3")
        self.horizontalLayout.addWidget(self.r3)
        self.r4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.r4.setFont(font)
        self.r4.setStyleSheet("")
        self.r4.setAlignment(QtCore.Qt.AlignCenter)
        self.r4.setObjectName("r4")
        self.horizontalLayout.addWidget(self.r4)
        self.r5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.r5.setFont(font)
        self.r5.setStyleSheet("")
        self.r5.setAlignment(QtCore.Qt.AlignCenter)
        self.r5.setObjectName("r5")
        self.horizontalLayout.addWidget(self.r5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 530, 761, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.is_valid = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.is_valid.setFont(font)
        self.is_valid.setObjectName("is_valid")
        self.horizontalLayout_3.addWidget(self.is_valid)
        self.check = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.horizontalLayout_3.addWidget(self.check)
        self.new_game = QtWidgets.QPushButton(self.centralwidget)
        self.new_game.setGeometry(QtCore.QRect(250, 20, 161, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.new_game.setFont(font)
        self.new_game.setObjectName("new_game")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 90, 761, 131))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.b1.setFont(font)
        self.b1.setStyleSheet("body {\n"
"    color: #a6780a\n"
"}")
        self.b1.setAlignment(QtCore.Qt.AlignCenter)
        self.b1.setObjectName("b1")
        self.horizontalLayout_2.addWidget(self.b1)
        self.b2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.b2.setFont(font)
        self.b2.setStyleSheet("")
        self.b2.setAlignment(QtCore.Qt.AlignCenter)
        self.b2.setObjectName("b2")
        self.horizontalLayout_2.addWidget(self.b2)
        self.b4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.b4.setFont(font)
        self.b4.setStyleSheet("")
        self.b4.setAlignment(QtCore.Qt.AlignCenter)
        self.b4.setObjectName("b4")
        self.horizontalLayout_2.addWidget(self.b4)
        self.b3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.b3.setFont(font)
        self.b3.setStyleSheet("")
        self.b3.setAlignment(QtCore.Qt.AlignCenter)
        self.b3.setObjectName("b3")
        self.horizontalLayout_2.addWidget(self.b3)
        self.b5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.b5.setFont(font)
        self.b5.setStyleSheet("")
        self.b5.setAlignment(QtCore.Qt.AlignCenter)
        self.b5.setObjectName("b5")
        self.horizontalLayout_2.addWidget(self.b5)
        self.who_win = QtWidgets.QLabel(self.centralwidget)
        self.who_win.setGeometry(QtCore.QRect(460, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.who_win.setFont(font)
        self.who_win.setStyleSheet("")
        self.who_win.setText("")
        self.who_win.setObjectName("who_win")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionReferense = QtWidgets.QAction(MainWindow)
        self.actionReferense.setObjectName("actionReferense")
        self.actionWrite_to_developers = QtWidgets.QAction(MainWindow)
        self.actionWrite_to_developers.setObjectName("actionWrite_to_developers")
        self.actionAbout_program = QtWidgets.QAction(MainWindow)
        self.actionAbout_program.setObjectName("actionAbout_program")
        self.menuFile.addAction(self.actionCreate)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionReferense)
        self.menuHelp.addAction(self.actionWrite_to_developers)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_program)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Keys - Beta 1.0"))
        self.p2.setText(_translate("MainWindow", "X"))
        self.p3.setText(_translate("MainWindow", "X"))
        self.p1.setText(_translate("MainWindow", "X"))
        self.p5.setText(_translate("MainWindow", "X"))
        self.p4.setText(_translate("MainWindow", "X"))
        self.e1.setText(_translate("MainWindow", "Export"))
        self.i1.setText(_translate("MainWindow", "Import"))
        self.e2.setText(_translate("MainWindow", "Export"))
        self.e4.setText(_translate("MainWindow", "Export"))
        self.e3.setText(_translate("MainWindow", "Export"))
        self.e5.setText(_translate("MainWindow", "Export"))
        self.i2.setText(_translate("MainWindow", "Import"))
        self.i3.setText(_translate("MainWindow", "Import"))
        self.i4.setText(_translate("MainWindow", "Import"))
        self.i5.setText(_translate("MainWindow", "Import"))
        self.edit_lbl.setText(_translate("MainWindow", "Valids:"))
        self.edit_num.setText(_translate("MainWindow", "3"))
        self.lvl_lbl.setText(_translate("MainWindow", "Level:"))
        self.lvl_num.setText(_translate("MainWindow", "1"))
        self.r1.setText(_translate("MainWindow", "X"))
        self.r2.setText(_translate("MainWindow", "X"))
        self.r3.setText(_translate("MainWindow", "X"))
        self.r4.setText(_translate("MainWindow", "X"))
        self.r5.setText(_translate("MainWindow", "X"))
        self.is_valid.setText(_translate("MainWindow", "IS VALID?"))
        self.check.setText(_translate("MainWindow", "CHECK!"))
        self.new_game.setText(_translate("MainWindow", "New game"))
        self.b1.setText(_translate("MainWindow", "X"))
        self.b2.setText(_translate("MainWindow", "X"))
        self.b4.setText(_translate("MainWindow", "X"))
        self.b3.setText(_translate("MainWindow", "X"))
        self.b5.setText(_translate("MainWindow", "X"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionReferense.setText(_translate("MainWindow", "Referense"))
        self.actionWrite_to_developers.setText(_translate("MainWindow", "Write to developers"))
        self.actionAbout_program.setText(_translate("MainWindow", "About program"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())