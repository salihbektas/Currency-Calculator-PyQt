from PyQt5 import QtWidgets
import sys
import os
from CurrencyCalculatorUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json


url = "https://api.exchangeratesapi.io/latest?"

result = requests.get(url)

result = json.loads(result.text)

rates = result["rates"]
rates["EUR"] = "1.0"
currencies = list(rates.keys())
currencies.sort()


class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculateButton.clicked.connect(self.pressBtn)
        self.ui.comboBoxSource.addItems(currencies)
        self.ui.comboBoxSource.setCurrentIndex(8)
        self.ui.comboBoxSource.setStyleSheet("combobox-popup: 0;")
        self.ui.comboBoxTarget.addItems(currencies)
        self.ui.comboBoxTarget.setCurrentIndex(31)
        self.ui.comboBoxTarget.setStyleSheet("combobox-popup: 0;")
        temp = rates["USD"] *100
        temp = int(temp)
        temp/= 100
        self.ui.target.setText(str(temp))
        
    
    def pressBtn(self):
        target = self.ui.comboBoxTarget.currentText()
        source = self.ui.comboBoxSource.currentText()
        money = self.ui.source.text()
        temp = str()
        for i in money:
            if i != ',':
                temp = temp + i
            else:
                temp = temp + '.'
        money = temp
        money = float(money)
        money /= float(rates[source])
        money *= float(rates[target])
        money *= 100
        i = 0
        while money<1:
            money *= 100
            i += 1
        money = int(money)
        money /= 100
        while i > 0:
            money /= 100
            i -= 1
        self.ui.target.setText(str(money))





calculator = QtWidgets.QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(calculator.exec())