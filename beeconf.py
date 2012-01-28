import sys
import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyKDE4.kio import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    

    

        
class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName(_fromUtf8("MainWin"))
        MainWin.resize(407, 292)
        MainWin.setWindowTitle(QtGui.QApplication.translate("MainWin", "Beeconf", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 391, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.chooser = QtGui.QPushButton(self.widget)
        self.chooser.setEnabled(True)
        self.chooser.setText(QtGui.QApplication.translate("MainWin", "Choose Application..", None, QtGui.QApplication.UnicodeUTF8))
        self.chooser.setCheckable(False)
        self.chooser.setDefault(False)
        self.chooser.setFlat(False)
        self.chooser.setObjectName(_fromUtf8("chooser"))
        self.horizontalLayout.addWidget(self.chooser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.radioGroup = QtGui.QGroupBox(self.widget)
        self.radioGroup.setTitle(QtGui.QApplication.translate("MainWin", "Choose the default GPU for this program", None, QtGui.QApplication.UnicodeUTF8))
        self.radioGroup.setObjectName(_fromUtf8("radioGroup"))
        self.widget1 = QtGui.QWidget(self.radioGroup)
        self.widget1.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.r1 = QtGui.QRadioButton(self.widget1)
        self.r1.setEnabled(0)
        self.r1.setText(QtGui.QApplication.translate("MainWin", "Intel GPU", None, QtGui.QApplication.UnicodeUTF8))
        self.r1.setObjectName(_fromUtf8("r1"))
        self.horizontalLayout_2.addWidget(self.r1)
        self.r2 = QtGui.QRadioButton(self.widget1)
        self.r2.setEnabled(0)
        self.r2.setText(QtGui.QApplication.translate("MainWin", "nVidia GPU", None, QtGui.QApplication.UnicodeUTF8))
        self.r2.setObjectName(_fromUtf8("r2"))
        self.horizontalLayout_2.addWidget(self.r2)
        self.applyButton = QtGui.QPushButton(self.widget1)
        #self.applyButton.setEnabled(0)
        self.applyButton.setText(QtGui.QApplication.translate("MainWin", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout_2.addWidget(self.applyButton)
        self.verticalLayout.addWidget(self.radioGroup)
        self.closeButton = QtGui.QDialogButtonBox(self.widget)
        self.closeButton.setOrientation(QtCore.Qt.Horizontal)
        self.closeButton.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.closeButton.setCenterButtons(False)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)
        MainWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWin.setStatusBar(self.statusbar)
        self.appPath=''
        self.appName=''
        self.flag=1
        
        
        self.retranslateUi(MainWin)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), MainWin.close)
        QtCore.QObject.connect(self.applyButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.applyChanges)
        
        QtCore.QObject.connect(self.chooser, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDial)
        
        QtCore.QMetaObject.connectSlotsByName(MainWin)
    
    def isOpti(self, filename):
      f1=open(filename)
      f=f1.readlines()
      falag=0
      for line in f:
	if line.startswith("Exec=") and ("optirun" in line):
	  falag = 1
	  break;
      return falag
  
  
    def isLocal(self, filename):
      if(os.path.dirname(str(filename)).startswith(os.environ['HOME'])):
	return 1
      else:
	return 0
    
    def convertToOpti(self, filename):
      tempfile=os.path.join(os.path.dirname(str(filename)),'~' + os.path.basename(str(filename)))
      f1=open(filename)
      f=f1.read()
      f = f.replace("Exec=","Exec=optirun ")
      f1.close()
  
      if self.isLocal(filename):
	f2 = open(tempfile, 'w')
	f2.write(f)
	f2.close()
	os.rename(tempfile,filename)
    
    
      else:
	newdir=os.path.join(os.environ['HOME'],'.local/share/applications/')
	if(os.path.dirname(str(filename)).endswith('kde4/')):
	  newdir=os.path.join(newdir,'kde4/')
	newpath=os.path.join(newdir,os.path.basename(str(filename)))
	f2 = open(newpath, 'w')
	f2.write(f)
	f2.close()
	self.appPath=newpath
    

    def removeOpti(self, filename):
      tempfile=os.path.join(os.path.dirname(str(filename)),'~' + os.path.basename(str(filename)))
      f1=open(filename)
  
      f=f1.read()
      f = f.replace("optirun", "")
      ''' What the fuck?
      f=f1.readlines()
      for line in f:
	if line.startswith("Exec=") and ("optirun" in line):
	  print "found"
	  if(line.replace("optirun"," ")):
	    print"removed 1 instance"
	f2.write(line)'''
      if self.isLocal(filename):
	f2 = open(tempfile, 'w')
	f2.write(f)
	f2.close()
	os.rename(tempfile,filename)
    
    
      else:
	newdir=os.path.join(os.environ['HOME'],'.local/share/applications/')
	if(os.path.dirname(str(filename)).endswith('kde4/')):
	  newdir=os.path.join(newdir,'kde4/')
	newpath=os.path.join(newdir,os.path.basename(str(filename)))
	f2 = open(newpath, 'w')
	f2.write(f)
	f2.close()
	self.appPath=newpath
        
    def miscui(self,filename):
      
      if(self.isOpti(filename)):
	
	self.r2.setChecked(1)
	
      else:
	
	self.r1.setChecked(1)
	
      
    
    def showDial(self):
      self.statusbar.clearMessage()
      odialog=KOpenWithDialog()
      odialog.hideNoCloseOnExit()
      odialog.hideRunInTerminal()
      odialog.setSaveNewApplications(1)
      
      odialog.exec_()
      if(odialog.service()):
	self.r1.setEnabled(1)
	self.r2.setEnabled(1)
	self.flag=0
	self.appName=odialog.service().desktopEntryName()
	self.appPath=odialog.service().entryPath()
	self.lineEdit.setText(self.appName)
	self.miscui(self.appPath)
	
      
	
      
    def applyChanges(self):
      if(self.flag):
	return 0
      filename=self.appPath
      if(self.r1.isChecked()):
	if(self.isOpti(filename)):
	  self.removeOpti(filename)
	  self.statusbar.clearMessage()
	  self.statusbar.showMessage("Default GPU for selected application is now Intel")
	else:
	  self.statusbar.clearMessage()
	  self.statusbar.showMessage("Default GPU for selected application is already Intel")
       
      elif(self.r2.isChecked()):
	if(self.isOpti(filename)):
	  
	  self.statusbar.showMessage("Default GPU is for selected application already nVidia")
	else:
	  self.convertToOpti(filename)
	  self.statusbar.clearMessage()
	  self.statusbar.showMessage("Default GPU is for selected application now nVidia")

      else:
	self.statusbar.clearMessage()
	self.statusbar.showMessage("Invalid option selected")
	
      

    def retranslateUi(self, MainWin):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWin = QtGui.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())

