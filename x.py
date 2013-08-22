# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app22.ui'
#
# Created: Tue Jan  1 00:12:15 2002
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import requests

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(664, 595)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 311, 121))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 26, 201, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 201, 31))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(340, 80, 311, 121))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 26, 201, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 70, 201, 31))
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 141, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 60, 101, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 210, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(10, 220, 161, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 280, 641, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 340, 461, 41))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 340, 51, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 310, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 340, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(320, 420, 20, 121))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 430, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 490, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 440, 301, 91))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.slot1)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.slot2)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.slot5)
	QtCore.QMetaObject.connectSlotsByName(MainWindow)
	try:
		f=open("./.ssh/remember.txt","r")
		list=[]
		for line in f:
			list.append(line[:-1])
		self.lineEdit.setText(list[0])
		self.lineEdit_2.setText(list[1])
		self.lineEdit_3.setText(list[2])
		self.lineEdit_4.setText(list[3])
	except IOError:
		return

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400; font-style:normal;\">Username</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Password</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400; font-style:normal;\">Username</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Password</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "User Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Proxy Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Remember me", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "..........", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:400; font-style:normal;\">Get Directory</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Start Syncing", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Stop Syncing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Message Box", None, QtGui.QApplication.UnicodeUTF8))
    def login(self):
	self.textEdit.setText("")
	try:
		f=open('./.ssh/id_rsa.pub','r')
		z=f.read()
		z=z[:-1]
	except IOError:
		self.textEdit.setText("Install ssh server")	
        x=str(self.lineEdit.text())
        y=str(self.lineEdit_2.text())
        try:
        	fr=open("./.ssh/"+x+"_log.txt")
        	n=1
        except IOError:
        	fr=open("./.ssh/"+x+"_log.txt","w")
    		n=0
        if(x=='')or(y==''):
        	self.textEdit.setText("Enter username and password")	
	else:
		if(str(self.lineEdit_3.text())=='' or str(self.lineEdit_4.text())==''):
			self.textEdit.setText("Enter proxy Settings")
		else:
			c=str(self.lineEdit_3.text())
			w=str(self.lineEdit_4.text())
			http_proxy  = "http://"+c+":"+w+"@202.141.80.19:3128"
			https_proxy = "http://"+c+":"+w+"@202.141.80.19:3128"
			ftp_proxy   = "http://"+c+":"+w+"@202.141.80.19:3128"

			proxyDict = { 
				      "http"  : http_proxy, 
				      "https" : https_proxy, 
				      "ftp"   : ftp_proxy
				    }
			if(n==1):
				z=""
			payload={'username':x, 'password':y,'key':z}
			try:
				r = requests.post('http://172.16.26.79:8001/desk/', data=payload, proxies=proxyDict,timeout=10)
			except:
				self.textEdit.setText("Connection Timeout!!!Make sure proxy settings are correct!!Contract your network provider for further clarification!!!Restart!!!")
				return
			st=r.text
			st=st[13:-3]
			if(st=='User is valid, active and authenticate'):
				self.textEdit.setText("Successfull Authentication")
				self.pushButton_3.setEnabled(True)
				self.lineEdit.setReadOnly(True)
				self.lineEdit_2.setReadOnly(True)
			elif(st=='The password is valid, but the account has been disabled'):
				self.textEdit.setText("Account is disabled")
			
			elif(st=='The username and password were incorrect'):
				self.textEdit.setText("Incorrect query")
			
    def slot1(self):
	self.lineEdit_5.setText(QtGui.QFileDialog.getExistingDirectory())
	path=str(self.lineEdit_5.text())
	if(path!=''):
		self.textEdit.setText("Once you click the Done button the path will be set!!Be Careful!!!")
    def slot2(self):
	if(str(self.lineEdit_5.text())==''):
		self.textEdit.setText("Please select a directory to sync")
		return
	try:
		f=open("./.unison/test.prf","w")
		path=str(self.lineEdit_5.text())
		u=str(self.lineEdit.text())
		f.write("root = ssh://wall@172.16.26.79/Documents/main/blob/blob/media/pictures/%s/\nroot = %s\nbatch = true\nauto = true\n"%(u,path))
		f.close()
		state=str(self.checkBox.checkState())
		if(state=='2'):
			print "yes"
			f=open("./.ssh/remember.txt","w")
			f.write("%s\n%s\n%s\n%s\n"%(str(self.lineEdit.text()),str(self.lineEdit_2.text()),str(self.lineEdit_3.text()),str(self.lineEdit_4.text())))
		else:
			try:
				f=open("./.ssh/remember.txt")
				f.close()
				os.remove("./.ssh/remember.txt")
			except IOError:
				self.pushButton_4.setEnabled(True)
				self.pushButton_5.setEnabled(True)
		self.pushButton_4.setEnabled(True)
		self.pushButton_5.setEnabled(True)
		return
	except IOError:
		self.textEdit.setText("Error:Install unison for file sharing")
    def slot5(self):
    	print "yes"
     	f=open("./.ssh/main.sh","w")
     	print "yes2"
     	f.write("#!/bin/bash\nunison test\nwhile inotifywait -e create -e moved_to -e moved_from -e attrib -e move_self -e delete -e modify -r $1\ndo\nunison test\ndone")
	print "yes3"
	f.close()
	print "yes4"
	if(str(self.lineEdit_5.text())==''):
		print "no"
		self.textEdit.setText("Please select a directory to sync")
		return
	else:
		print "no"
		ret=subprocess.call("chmod 777 ./.ssh/main.sh",shell=True)
		i1='gnome-terminal --command="./.ssh/main.sh '+str(self.lineEdit_5.text())+'"'
		ret2=subprocess.Popen(i1,shell=True)
   		print "done1"
   		
   		print "done"
if __name__ == "__main__":
    import sys
    import subprocess
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
