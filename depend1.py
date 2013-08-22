#! /usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depend1.ui'
#
# Created: Sat Mar 30 16:49:03 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 181, 27))
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 60, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 120, 381, 161))
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.install)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Enter login-password", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Get Started", None, QtGui.QApplication.UnicodeUTF8))

    def install(self):
	self.plainTextEdit.clear()
	x=str(self.lineEdit.text())
	
	installer1="echo "+x+" | sudo -S apt-get -y install unison"
	installer2="echo "+x+" | sudo -S apt-get -y install openssh-client"
	installer3="echo "+x+" | sudo -S apt-get -y install inotify-tools"
	installer4="echo .ssh/id_rsa | ssh-keygen"
	find_file="find ~ -name x.desktop 2>/dev/null"
	
	ret=subprocess.call( installer1, shell = True)
	#output1 = int(subprocess.Popen( 'echo $?', stdout=subprocess.PIPE, shell = True ).communicate()[0]) 
	if(ret==1):
		self.plainTextEdit.appendPlainText(_fromUtf8("Installation of package 'unison' unsuccessful. Please ensure that password is correct."))
		return
	else:
		self.plainTextEdit.appendPlainText(_fromUtf8("Installation of package 'unison' successful."))
	ret=subprocess.call( installer2, shell = True)
	#output1 = int(subprocess.Popen( 'echo $?', stdout=subprocess.PIPE, shell = True ).communicate()[0]) 
	if(ret==1):
		self.plainTextEdit.appendPlainText(_fromUtf8("Installation of package 'openssh-client' unsuccessful. Please ensure that password is correct."))
		return
	else:
		self.plainTextEdit.appendPlainText(_fromUtf8("Installation of package 'openssh-client' successful."))
	ret=subprocess.call( installer3, shell = True)
	#output1 = int(subprocess.Popen( 'echo $?', stdout=subprocess.PIPE, shell = True ).communicate()[0]) 
	if(ret==1):
		self.plainTextEdit.appendPlainText(_fromUtf8("Installation of package 'inotify-tools' unsuccessful. Please ensure that password is correct."))
		return
	else:
		self.plainTextEdit.appendPlainText(_fromUtf8("Installation of package 'inotify-tools' successful."))
	filepath = subprocess.check_output(find_file , shell=True)
	filepath = filepath.splitlines()
	filepath = filepath[0]
	installer5="mv "+filepath+" ~/.config/autostart"
	ret=subprocess.call( installer5, shell = True)
	#output1 = int(subprocess.Popen( 'echo $?', stdout=subprocess.PIPE, shell = True ).communicate()[0]) 
	if(ret==1):
		self.plainTextEdit.appendPlainText(_fromUtf8("Auto-run couldn't be activated"))
		return
	else:
		self.plainTextEdit.appendPlainText(_fromUtf8("Auto-run activated"))
	ret=subprocess.call( installer4, shell = True)
	#output1 = int(subprocess.Popen( 'echo $?', stdout=subprocess.PIPE, shell = True ).communicate()[0]) 
	if(ret==1):
		self.plainTextEdit.appendPlainText(_fromUtf8("ssh-key generation unsuccessful. Please delete the id_rsa.pub file, if already exists!"))
		return
	else:
		self.plainTextEdit.appendPlainText(_fromUtf8("ssh-key generation successful."))
	


if __name__ == "__main__":
    import subprocess
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

