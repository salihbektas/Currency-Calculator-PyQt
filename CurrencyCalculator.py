from PyQt5 import QtWidgets
import sys
import os
from CurrencyCalculatorUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

#Get lates currency rates
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
        #load currencies to combo boxes
        self.ui.comboBoxSource.addItems(currencies)
        self.ui.comboBoxTarget.addItems(currencies)
        self.ui.comboBoxSource.setStyleSheet("combobox-popup: 0;")
        self.ui.comboBoxTarget.setStyleSheet("combobox-popup: 0;")
        #select EUR on source combo box(currencies[8] is EUR)
        self.ui.comboBoxSource.setCurrentIndex(8)
        #select USD on target combo box(currencies[31] is USD)
        self.ui.comboBoxTarget.setCurrentIndex(31)
        #Calculates the USD value of 1 EUR with the two digits after the dot
        temp = rates["USD"] *100
        temp = int(temp)
        temp/= 100
        self.ui.target.setText(str(temp))
        
    
    def pressBtn(self):
        target = self.ui.comboBoxTarget.currentText()
        source = self.ui.comboBoxSource.currentText()
        money = self.ui.source.text()

        #extracts commas from user's input
        temp = str()
        for i in money:
            if i != ',':
                temp = temp + i
            else:
                temp = temp + '.'
        
        #calculate from the desired currency with the two digits after the dot
        #if the result is less than 0.01, the calculation is made in the
        #smaller unit than the two digits after the point.
        money = temp
        money = float(money)
        money /= float(rates[source])
        money *= float(rates[target])
        money *= 100

        i = 0
        while money < 1:
            money *= 100
            i += 1

        money = int(money)
        money /= 100

        while i > 0:
            money /= 100
            i -= 1

        #write result to target label    
        self.ui.target.setText(str(money))


#Main
calculator = QtWidgets.QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(calculator.exec())