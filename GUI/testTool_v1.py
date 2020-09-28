#! /usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import time
import psutil
import os

import serial.tools.list_ports

import threading

BAUDRATES = ["50", "75", "110", "134", "150", "200", "300", "600", "1200", "1800", "2400", "4800",
             "9600", "19200", "38400", "57600", "115200"]
test = ['11', '22']

connection = serial.Serial()
event_thread=threading.Event()

test1_stat = False
test2_stat = False

VERSION = "Version 1.0"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(530, 596)
        MainWindow.setFixedSize(530,600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Group boxes
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 201, 131))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 251, 391))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QtCore.QRect(280, 10, 241, 131))
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QtCore.QRect(280, 160, 241, 391))

        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(100, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        a = [port[0] for port in serial.tools.list_ports.comports()]
        for a in a:
            self.comboBox.addItem(a)

        self.refreshCom = QPushButton(self.groupBox)
        self.refreshCom.setObjectName("refreshCom")
        self.refreshCom.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.refreshCom.clicked.connect(self.refresh_comm)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 81, 13))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 81, 13))
        self.label_6.setObjectName("label_6")

        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 60, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_2.addItem("9600")

        #BUTTONS
        #open serial connection
        self.openPortButton = QtWidgets.QPushButton(self.groupBox)
        self.openPortButton.setGeometry(QtCore.QRect(100, 100, 71, 21))
        self.openPortButton.setObjectName("openPortButton")
        self.openPortButton.clicked.connect(self.openPort)

        #Testbutton test 1
        self.pushButton_t1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_t1.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.pushButton_t1.setObjectName("pushButton")
        self.pushButton_t1.setEnabled(False)
        self.pushButton_t1.clicked.connect(self.test1)
        #self.pushButton.clicked.connect(self.test1_button)

        #Testbutton test 2
        self.pushButton_t2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_t2.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.pushButton_t2.setObjectName("pushButton_2")
        self.pushButton_t2.setEnabled(False)
        self.pushButton_t2.clicked.connect(self.test2)

        #Testbutton test 3
        self.pushButton_t3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_t3.setGeometry(QtCore.QRect(100, 100, 75, 23))
        self.pushButton_t3.setObjectName("pushButton_3")
        self.pushButton_t3.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #reset log button
        self.clear_log = QtWidgets.QPushButton(self.groupBox_4)
        self.clear_log.setObjectName(u"clear_log")
        self.clear_log.setGeometry(QtCore.QRect(10, 360, 75, 23))
        self.clear_log.clicked.connect(self.log_reset)

        #Buttons status
        self.status_t1 = QtWidgets.QPushButton(self.groupBox_2)
        self.status_t1.setObjectName(u"status_t1")
        self.status_t1.setGeometry(QtCore.QRect(180, 20, 21, 21))
        self.status_t2 = QtWidgets.QPushButton(self.groupBox_2)
        self.status_t2.setObjectName(u"status_t2")
        self.status_t2.setGeometry(QtCore.QRect(180, 60, 21, 21))
        self.status_t3 = QtWidgets.QPushButton(self.groupBox_2)
        self.status_t3.setObjectName(u"status_t3")
        self.status_t3.setGeometry(QtCore.QRect(180, 100, 21, 21))

        #Log wigets
        self.listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 221, 331))
        self.listWidget.setAutoScroll(True)
        self.listWidget.addItem("NADD test system "+ VERSION)

        #detail labels
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QtCore.QRect(10, 110, 141, 16))
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.label_10.setPixmap(QPixmap("LargeFileManagerLogo.png"))
        self.label_10.setScaledContents(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test tool ICS  --" + VERSION))

        self.label_2.setText(_translate("MainWindow", "Available Ports"))
        self.label_3.setText(_translate("MainWindow", "Baudrate"))
        self.openPortButton.setText(_translate("MainWindow", "OPEN"))

        self.groupBox.setTitle(_translate("MainWindow", "Serial settings"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Test options"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Details"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Test log"))

        self.pushButton_t1.setText(_translate("MainWindow", "START"))
        self.pushButton_t2.setText(_translate("MainWindow", "START"))
        self.pushButton_t3.setText(_translate("MainWindow", "START"))

        self.clear_log.setText(_translate("MainWindow", "Clear log"))

        self.refreshCom.setText(_translate("MainWindow", "Refresh"))

        self.label_4.setText(_translate("MainWindow", "SD card test"))
        self.label_5.setText(_translate("MainWindow", "EEPROM test"))
        self.label_6.setText(_translate("MainWindow", "IO test"))

        #detail label
        self.label_7.setText(_translate("MainWindow", "Hacousto Protec"))
        self.label_8.setText(_translate("MainWindow", VERSION))
        self.label_9.setText(_translate("MainWindow", "Made by :  Niels van Hagen"))
        self.label_10.setText("")

        self.status_t1.setText("")
        self.status_t2.setText("")
        self.status_t3.setText("")


    def refresh_comm(self):
        self.comboBox.clear()
        a = [port[0] for port in serial.tools.list_ports.comports()]
        for a in a:
            self.comboBox.addItem(a)

    def openPort(self):
        print("Opening Serial port")
        print(self.comboBox.currentText())

        self.log_reset()

        if not(connection.is_open):
            connection.baudrate = self.comboBox_2.currentText()
            connection.port = self.comboBox.currentText()
            connection.open()
            if (connection.is_open):
                self.openPortButton.setStyleSheet("background-color: green")
                self.openPortButton.setText(QtCore.QCoreApplication.translate("MainWindow", "CLOSE"))

                #Disable widgets
                self.comboBox.setEnabled(False)
                self.comboBox_2.setEnabled(False)
                self.refreshCom.setEnabled(False)

                #Enable test buttons
                self.pushButton_t1.setEnabled(True)
                self.pushButton_t2.setEnabled(True)
                self.pushButton_t3.setEnabled(True)
                #Log update

            else:
                msg = QMessageBox()
                msg.setWindowTitle("ERROR - COM CONNECTION")
                msg.setText("Could not connect with com port!")
                x = msg.exec_()
        elif (connection.is_open):
            connection.close()
            if not(connection.is_open):
                self.close_connection()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("ERROR - COM CONNECTION")
                msg.setText("Could not disconnect with com port!")
                x = msg.exec_()

        print(connection.is_open)

    def close_connection(self):
        self.openPortButton.setStyleSheet("default")
        self.openPortButton.setText(QtCore.QCoreApplication.translate("MainWindow", "OPEN"))

        #set all layout to default
        self.set_test_default()

        #Reset status indicatiors:
        self.status_t1.setStyleSheet("default")
        self.status_t2.setStyleSheet("default")
        self.status_t3.setStyleSheet("default")

        self.pushButton_t1.setEnabled(False)
        self.pushButton_t2.setEnabled(False)
        self.pushButton_t3.setEnabled(False)

        #Stop event listener
        self.event_thread.set()

    def test1(self):
        print("com port:")
        print(connection.isOpen())
        global test1_stat

        if not(test1_stat):
            try:
                connection.port = self.comboBox.currentText()

                connection.close()
                connection.open()
                self.log_reset()
                self.listWidget.addItem('Starting test 1...')

                self.status_t1.setStyleSheet("background-color: orange")
                test1_stat = True

                #Start test
                print("Writing to teensy...")
                connection.write(b'1')

                #Button conf
                self.pushButton_t1.setText("STOP")
                self.pushButton_t2.setEnabled(False)
                self.pushButton_t3.setEnabled(False)

                #starting thread test
                # global event_thread
                self.event_thread=threading.Event()
                self.c_thread=threading.Thread(target=self.myEvenListener, args=(event_thread,))
                self.c_thread.start()
            except serial.serialutil.SerialException:
                msg = QMessageBox()
                msg.setWindowTitle("ERROR - COM CONNECTION")
                msg.setText("Could not connect with com port!")
                x = msg.exec_()
                self.close_connection()
        elif(test1_stat):

            #Button conf
            self.pushButton_t1.setText("START")
            self.pushButton_t2.setEnabled(True)
            self.pushButton_t3.setEnabled(True)

            test1_stat = False

            self.event_thread.set()

    def test2(self):
        print("com port:")
        print(connection.isOpen())
        global test2_stat

        if not(test2_stat):
            try:
                connection.port = self.comboBox.currentText()

                connection.close()
                connection.open()
                self.log_reset()
                self.listWidget.addItem('Starting test 2...')

                self.status_t2.setStyleSheet("background-color: orange")
                test2_stat = True

                #Start test
                print("Writing to teensy...")
                connection.write(b'2')

                #Button conf
                self.pushButton_t1.setEnabled(False)
                self.pushButton_t2.setText("STOP")
                self.pushButton_t3.setEnabled(False)

                #starting thread test
                # global event_thread
                self.event_thread=threading.Event()
                self.c_thread=threading.Thread(target=self.myEvenListener, args=(event_thread,))
                self.c_thread.start()
            except serial.serialutil.SerialException:
                msg = QMessageBox()
                msg.setWindowTitle("ERROR - COM CONNECTION")
                msg.setText("Could not connect with com port!")
                x = msg.exec_()
                self.close_connection()
        elif(test2_stat):

            #Button conf
            self.pushButton_t1.setEnabled(True)
            self.pushButton_t2.setText("START")
            self.pushButton_t3.setEnabled(True)

            test2_stat = False

            self.event_thread.set()


    def set_test_default(self):
        #Enable widgets
        self.comboBox.setEnabled(True)
        self.comboBox_2.setEnabled(True)
        self.refreshCom.setEnabled(True)

        #Disable test buttons
        self.pushButton_t1.setEnabled(True)
        self.pushButton_t2.setEnabled(True)
        self.pushButton_t3.setEnabled(True)

        self.pushButton_t1.setText("START")
        self.pushButton_t2.setText("START")
        self.pushButton_t3.setText("START")

    #Thread event for data reading
    def myEvenListener(self,event_thread):
        state=True
        global test1_stat
        while state and not event_thread.isSet():
            data = connection.readline()[:-2] #the last bit gets rid of the new-line chars
            print(data)
            if(data == bytes('T1-t', encoding='utf-8')):
                print("Test 1 complete --ack")
                self.status_t1.setStyleSheet("background-color: green")
                self.set_test_default()
                test1_stat = False
            elif(data == bytes('T1-f', encoding='utf-8')):
                print("Test 1 failed --ack")
                self.status_t1.setStyleSheet("background-color: red")
                self.set_test_default()
                test1_stat = False
            elif(data == bytes('T2-t', encoding='utf-8')):
                print("Test 2 complete --ack")
                self.status_t2.setStyleSheet("background-color: green")
                self.set_test_default()
                test2_stat = False
            elif(data == bytes('T2-f', encoding='utf-8')):
                print("Test 2 failed --ack")
                self.status_t2.setStyleSheet("background-color: red")
                self.set_test_default()
                test2_stat = False
            elif data:
                self.listWidget.addItem(str(data.decode("utf-8")))
                print(data)

    def stop_event(self):
        self.event_thread.set()
        print(self.event_thread.isSet())

    #Log functions
    def log_update(line):
        listWidget.addItem(line)

    def log_reset(self):
        self.listWidget.clear()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
