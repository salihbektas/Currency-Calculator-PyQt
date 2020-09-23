# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CurrencyCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 203)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 370, 237, 25))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 10, 321, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.target = QtWidgets.QLabel(self.gridLayoutWidget)
        self.target.setFrameShape(QtWidgets.QFrame.Box)
        self.target.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.target.setObjectName("target")
        self.gridLayout.addWidget(self.target, 1, 0, 1, 1)
        self.source = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.source.setMaxLength(14)
        self.source.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.source.setObjectName("source")
        self.gridLayout.addWidget(self.source, 0, 0, 1, 1)
        self.comboBoxTarget = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxTarget.setMaxVisibleItems(9)
        self.comboBoxTarget.setObjectName("comboBoxTarget")
        self.gridLayout.addWidget(self.comboBoxTarget, 1, 1, 1, 1)
        self.comboBoxSource = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxSource.setMaxVisibleItems(9)
        self.comboBoxSource.setMinimumContentsLength(0)
        self.comboBoxSource.setObjectName("comboBoxSource")
        self.gridLayout.addWidget(self.comboBoxSource, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 90)
        self.gridLayout.setColumnStretch(1, 10)
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(300, 120, 91, 25))
        self.calculateButton.setObjectName("calculateButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Calculator"))
        self.target.setText(_translate("MainWindow", "1"))
        self.source.setText(_translate("MainWindow", "1.00"))
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
