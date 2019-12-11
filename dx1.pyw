import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("main.ui")[0]

class WindowClass(QMainWindow, from_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.fontSize = 10
		# self.btn1.clicked.connect(self.btn1_func)
		# self.btn2.clicked.connect(self.btn2_func)

		self.rdo1.clicked.connect(self.gBoxFunc)
		self.rdo2.clicked.connect(self.gBoxFunc)
		self.rdo3.clicked.connect(self.gBoxFunc)
		self.rdo4.clicked.connect(self.gBoxFunc)

		self.chk1.stateChanged.connect(self.chkFunc)
		self.chk2.stateChanged.connect(self.chkFunc)
		self.chk3.stateChanged.connect(self.chkFunc)
		self.chk4.stateChanged.connect(self.chkFunc)

		self.btn1.clicked.connect(self.change_txt_Func)

		self.btn2.clicked.connect(self.btn2_txtPrint)
		self.btn3.clicked.connect(self.btn3_setText)
		self.btn4.clicked.connect(self.btn4_txtAppend)
		self.btn5.clicked.connect(self.btn5_txtClear)

		self.le.textChanged.connect(self.le_setlbl)
		self.le.returnPressed.connect(self.le_print)
		self.btn6.clicked.connect(self.btn6_ch_txt)

		self.btn7.clicked.connect(self.btn7_setFont)

		self.btn8.clicked.connect(self.btn8_setFontUp)
		self.btn9.clicked.connect(self.btn9_setFontDown)

		self.syncComboBox()

		self.combo1.currentIndexChanged.connect(self.comboBoxFunction)

		self.btn_print.clicked.connect(self.printComboBoxItem)
		self.btn_clear.clicked.connect(self.clearComboBoxItem)
		self.btn_add.clicked.connect(self.addComboBoxItem)
		self.btn_delete.clicked.connect(self.deleteComboBoxItem)

	def syncComboBox(self):
		for i in range(0, self.combo1.count()):
			self.combo2.addItem(self.combo1.itemText(i))

	def comboBoxFunction(self):
		self.lbl_display.setText(self.combo1.currentText())

	def clearComboBoxItem(self):
		self.combo1.clear()
		self.combo2.clear()

	def printComboBoxItem(self):
		print(self.combo2.currentText())

	def addComboBoxItem(self):
		self.combo1.addItem(self.le01.text())
		self.combo2.addItem(self.le01.text())
		print("Item Added")

	def deleteComboBoxItem(self):
		self.del_idx = self.combo2.currentIndex()
		self.combo1.removeItem(self.del_idx)
		self.combo2.removeItem(self.del_idx)
		print("Item Deleted")
		

	def btn9_setFontDown(self):
		self.fontSize = self.fontSize - 1
		print(self.fontSize)
		self.textBrowser.setFontPointSize(self.fontSize)


	def btn8_setFontUp(self):
		self.fontSize = self.fontSize + 1 
		print(self.fontSize)
		self.textBrowser.setFontPointSize(self.fontSize)

	def btn7_setFont(self):
		fontvar = QFont("Apple SD Gothic Neo", 20)
		colorvar = QColor(255,0,0)

		self.textBrowser.setCurrentFont(fontvar)
		self.textBrowser.setFontItalic(True)
		self.textBrowser.setTextColor(colorvar)



	def le_setlbl(self):
		self.lbl2.setText(self.le.text())

	def le_print(self):
		print(self.le.text())

	def btn6_ch_txt(self):
		self.le.setText("Change Text")

	def btn2_txtPrint(self):
		self.lbl1.setText(self.textBrowser.toPlainText())

	def btn3_setText(self):
		self.textBrowser.setPlainText("Setting")

	def btn4_txtAppend(self):
		self.textBrowser.append(" Appending")

	def btn5_txtClear(self):
		self.textBrowser.clear()



	# def btn1_func(self):
	# 	print("btn 1 Clicked")

	# def btn2_func(self):
	# 	print("btn 2 Clicked")
	def change_txt_Func(self):
		self.lbl1.clear()
		self.btn1.setText("self.lbl1.text()")
		self.lbl1.setText("Change Text")

	def chkFunc(self):
		if self.chk1.isChecked() : print("Chk1")
		elif self.chk2.isChecked() : print("Chk2")
		elif self.chk3.isChecked() : print("Chk3")
		elif self.chk4.isChecked() : print("Chk4")

	def gBoxFunc(self):
		if self.rdo1.isChecked(): print("Rdo1")
		elif self.rdo2.isChecked(): print("Rdo2")
		elif self.rdo3.isChecked(): print("Rdo3")
		elif self.rdo4.isChecked(): print("Rdo4")

if __name__ == "__main__":

	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
