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
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: #303030; \n"
"color: #ffa550;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 450, 1221, 182))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(0, 180))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ps = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ps.setContentsMargins(0, 0, 0, 0)
        self.ps.setObjectName("ps")
        self.p1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1.setMinimumSize(QtCore.QSize(40, 180))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.p1.setFont(font)
        self.p1.setObjectName("p1")
        self.ps.addWidget(self.p1, 0, 0, 1, 1)
        self.p3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p3.setMinimumSize(QtCore.QSize(40, 180))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.p3.setFont(font)
        self.p3.setText("")
        self.p3.setObjectName("p3")
        self.ps.addWidget(self.p3, 0, 2, 1, 1)
        self.p2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p2.setMinimumSize(QtCore.QSize(40, 180))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.p2.setFont(font)
        self.p2.setText("")
        self.p2.setObjectName("p2")
        self.ps.addWidget(self.p2, 0, 1, 1, 1)
        self.p4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p4.setMinimumSize(QtCore.QSize(40, 180))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.p4.setFont(font)
        self.p4.setText("")
        self.p4.setObjectName("p4")
        self.ps.addWidget(self.p4, 0, 3, 1, 1)
        self.p5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p5.setMinimumSize(QtCore.QSize(40, 180))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.p5.setFont(font)
        self.p5.setText("")
        self.p5.setObjectName("p5")
        self.ps.addWidget(self.p5, 0, 4, 1, 1)
        self.edit_num = QtWidgets.QLabel(self.centralwidget)
        self.edit_num.setGeometry(QtCore.QRect(900, 0, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.edit_num.setFont(font)
        self.edit_num.setStyleSheet("")
        self.edit_num.setObjectName("edit_num")
        self.lvl_num = QtWidgets.QLabel(self.centralwidget)
        self.lvl_num.setGeometry(QtCore.QRect(1180, 0, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.lvl_num.setFont(font)
        self.lvl_num.setStyleSheet("")
        self.lvl_num.setObjectName("lvl_num")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 320, 1221, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.rs = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.rs.setContentsMargins(0, 0, 0, 0)
        self.rs.setObjectName("rs")
        self.r1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        self.r1.setFont(font)
        self.r1.setStyleSheet("")
        self.r1.setText("")
        self.r1.setAlignment(QtCore.Qt.AlignCenter)
        self.r1.setObjectName("r1")
        self.rs.addWidget(self.r1)
        self.r2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        self.r2.setFont(font)
        self.r2.setStyleSheet("")
        self.r2.setText("")
        self.r2.setAlignment(QtCore.Qt.AlignCenter)
        self.r2.setObjectName("r2")
        self.rs.addWidget(self.r2)
        self.r3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        self.r3.setFont(font)
        self.r3.setStyleSheet("")
        self.r3.setText("")
        self.r3.setAlignment(QtCore.Qt.AlignCenter)
        self.r3.setObjectName("r3")
        self.rs.addWidget(self.r3)
        self.r4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        self.r4.setFont(font)
        self.r4.setStyleSheet("")
        self.r4.setText("")
        self.r4.setAlignment(QtCore.Qt.AlignCenter)
        self.r4.setObjectName("r4")
        self.rs.addWidget(self.r4)
        self.r5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        self.r5.setFont(font)
        self.r5.setStyleSheet("")
        self.r5.setText("")
        self.r5.setAlignment(QtCore.Qt.AlignCenter)
        self.r5.setObjectName("r5")
        self.rs.addWidget(self.r5)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 160, 1221, 161))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.bs = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.bs.setContentsMargins(0, 0, 0, 0)
        self.bs.setObjectName("bs")
        self.b1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.b1.setFont(font)
        self.b1.setStyleSheet("body {\n"
"    color: #a6780a\n"
"}")
        self.b1.setText("")
        self.b1.setAlignment(QtCore.Qt.AlignCenter)
        self.b1.setObjectName("b1")
        self.bs.addWidget(self.b1)
        self.b2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.b2.setFont(font)
        self.b2.setStyleSheet("")
        self.b2.setText("")
        self.b2.setAlignment(QtCore.Qt.AlignCenter)
        self.b2.setObjectName("b2")
        self.bs.addWidget(self.b2)
        self.b4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.b4.setFont(font)
        self.b4.setStyleSheet("")
        self.b4.setText("")
        self.b4.setAlignment(QtCore.Qt.AlignCenter)
        self.b4.setObjectName("b4")
        self.bs.addWidget(self.b4)
        self.b3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.b3.setFont(font)
        self.b3.setStyleSheet("")
        self.b3.setText("")
        self.b3.setAlignment(QtCore.Qt.AlignCenter)
        self.b3.setObjectName("b3")
        self.bs.addWidget(self.b3)
        self.b5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.b5.setFont(font)
        self.b5.setStyleSheet("")
        self.b5.setText("")
        self.b5.setAlignment(QtCore.Qt.AlignCenter)
        self.b5.setObjectName("b5")
        self.bs.addWidget(self.b5)
        self.who_win = QtWidgets.QLabel(self.centralwidget)
        self.who_win.setGeometry(QtCore.QRect(280, 10, 441, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.who_win.setFont(font)
        self.who_win.setStyleSheet("")
        self.who_win.setText("")
        self.who_win.setAlignment(QtCore.Qt.AlignCenter)
        self.who_win.setObjectName("who_win")
        self.is_valid = QtWidgets.QPushButton(self.centralwidget)
        self.is_valid.setGeometry(QtCore.QRect(730, 0, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.is_valid.setFont(font)
        self.is_valid.setObjectName("is_valid")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(1010, 0, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.nex_lvl = QtWidgets.QPushButton(self.centralwidget)
        self.nex_lvl.setGeometry(QtCore.QRect(10, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.nex_lvl.setFont(font)
        self.nex_lvl.setObjectName("nex_lvl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuThemes = QtWidgets.QMenu(self.menuSettings)
        self.menuThemes.setObjectName("menuThemes")
        self.menuLocalization = QtWidgets.QMenu(self.menuSettings)
        self.menuLocalization.setObjectName("menuLocalization")
        self.menuFor_developers = QtWidgets.QMenu(self.menuSettings)
        self.menuFor_developers.setObjectName("menuFor_developers")
        self.menuWrite_logs = QtWidgets.QMenu(self.menuFor_developers)
        self.menuWrite_logs.setObjectName("menuWrite_logs")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewGame = QtWidgets.QAction(MainWindow)
        self.actionNewGame.setObjectName("actionNewGame")
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
        self.actionLight_mode = QtWidgets.QAction(MainWindow)
        self.actionLight_mode.setObjectName("actionLight_mode")
        self.actionNight_mode = QtWidgets.QAction(MainWindow)
        self.actionNight_mode.setObjectName("actionNight_mode")
        self.actionBlack_mode = QtWidgets.QAction(MainWindow)
        self.actionBlack_mode.setObjectName("actionBlack_mode")
        self.actionRUS = QtWidgets.QAction(MainWindow)
        self.actionRUS.setObjectName("actionRUS")
        self.actionENG = QtWidgets.QAction(MainWindow)
        self.actionENG.setObjectName("actionENG")
        self.actionInfinity_valid = QtWidgets.QAction(MainWindow)
        self.actionInfinity_valid.setObjectName("actionInfinity_valid")
        self.actionOn = QtWidgets.QAction(MainWindow)
        self.actionOn.setObjectName("actionOn")
        self.actionOff = QtWidgets.QAction(MainWindow)
        self.actionOff.setObjectName("actionOff")
        self.action3_sec = QtWidgets.QAction(MainWindow)
        self.action3_sec.setObjectName("action3_sec")
        self.action5_sec = QtWidgets.QAction(MainWindow)
        self.action5_sec.setObjectName("action5_sec")
        self.action10 = QtWidgets.QAction(MainWindow)
        self.action10.setObjectName("action10")
        self.action20_sec = QtWidgets.QAction(MainWindow)
        self.action20_sec.setObjectName("action20_sec")
        self.actionWhile_not_click_Level = QtWidgets.QAction(MainWindow)
        self.actionWhile_not_click_Level.setObjectName("actionWhile_not_click_Level")
        self.actionClick_on_Level = QtWidgets.QAction(MainWindow)
        self.actionClick_on_Level.setObjectName("actionClick_on_Level")
        self.menuFile.addAction(self.actionNewGame)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionReferense)
        self.menuHelp.addAction(self.actionWrite_to_developers)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_program)
        self.menuThemes.addAction(self.actionLight_mode)
        self.menuThemes.addAction(self.actionNight_mode)
        self.menuThemes.addAction(self.actionBlack_mode)
        self.menuLocalization.addAction(self.actionRUS)
        self.menuLocalization.addAction(self.actionENG)
        self.menuWrite_logs.addAction(self.actionOn)
        self.menuWrite_logs.addAction(self.actionOff)
        self.menuFor_developers.addAction(self.actionInfinity_valid)
        self.menuFor_developers.addAction(self.menuWrite_logs.menuAction())
        self.menuSettings.addAction(self.menuThemes.menuAction())
        self.menuSettings.addAction(self.menuLocalization.menuAction())
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.menuFor_developers.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Keys - Beta 2.0"))
        self.p1.setText(_translate("MainWindow", "10"))
        self.edit_num.setText(_translate("MainWindow", "3"))
        self.lvl_num.setText(_translate("MainWindow", "1"))
        self.is_valid.setText(_translate("MainWindow", "Valids:"))
        self.check.setText(_translate("MainWindow", "Level:"))
        self.nex_lvl.setText(_translate("MainWindow", "Continue"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuThemes.setTitle(_translate("MainWindow", "Themes"))
        self.menuLocalization.setTitle(_translate("MainWindow", "Localization"))
        self.menuFor_developers.setTitle(_translate("MainWindow", "For developers"))
        self.menuWrite_logs.setTitle(_translate("MainWindow", "Write logs"))
        self.actionNewGame.setText(_translate("MainWindow", "New game"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionReferense.setText(_translate("MainWindow", "Referense"))
        self.actionWrite_to_developers.setText(_translate("MainWindow", "Write to developers"))
        self.actionAbout_program.setText(_translate("MainWindow", "About program"))
        self.actionLight_mode.setText(_translate("MainWindow", "Light mode"))
        self.actionNight_mode.setText(_translate("MainWindow", "Night mode"))
        self.actionBlack_mode.setText(_translate("MainWindow", "Black mode"))
        self.actionRUS.setText(_translate("MainWindow", "RUS"))
        self.actionENG.setText(_translate("MainWindow", "ENG"))
        self.actionInfinity_valid.setText(_translate("MainWindow", "Infinity valid"))
        self.actionOn.setText(_translate("MainWindow", "On"))
        self.actionOff.setText(_translate("MainWindow", "Off"))
        self.action3_sec.setText(_translate("MainWindow", "3 sec"))
        self.action5_sec.setText(_translate("MainWindow", "5 sec"))
        self.action10.setText(_translate("MainWindow", "10 sec"))
        self.action20_sec.setText(_translate("MainWindow", "20 sec"))
        self.actionWhile_not_click_Level.setText(_translate("MainWindow", "Click on Level"))
        self.actionClick_on_Level.setText(_translate("MainWindow", "Click on Level"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
