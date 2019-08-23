# -*- coding: utf-8 -*-

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import logging
from logging.handlers import TimedRotatingFileHandler
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication


# luobo（2422973253@qq.com） 11.08.2019

# ---设置485主从站----
# 设定串口为从站
PORT = "com1"
master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
master.set_timeout(5.0)
master.set_verbose(True)

# ----读取485数据----
# 创建logger日志，可以指定参数名字，如果参数为空则返回root logger
logger = logging.getLogger('')
# 设置logger日志等级为INFO级别
logger.setLevel(logging.INFO)
# 设置Handler，将logger创建的日志记录发送到合适的目的输出
# 将日志消息发送到和程序同目录下的名luoborizhi的文件中，并按每2s时间切割，最多保留5个文件
logFilePath = 'luoborizhi'
handler = TimedRotatingFileHandler(logFilePath, when='s', interval=2, backupCount=5)
# 指定输出日志格式，时间+信息，
formatter = logging.Formatter('%(asctime)s-%(message)s')
handler.setFormatter(formatter)
# 将创建的handler添加到logger日志处理器
logger.addHandler(handler)
# 01数据 1站号 地址2001 长度1000的数据
while True:
    logger = modbus_tk.utils.create_logger("console")
    logger.info("connected")
    logger.info(master.execute(1, cst.READ_COILS, 2001, 1000))

    # ----处理485数据----
    with open('luoborizhi')as file_object:
        lines = file_object.readlines()  # 逐行读文件，存到表lines中
        n = len(lines)  # 获取表的长度
    for i in range(n):
        lines[i] = (lines[i])[24:50]  # 截取表第24项到末尾，保存到表
        if lines[i] == '-> 1-1-7-209-3-232-109-249' and (lines[i + 2])[24:25] == '(':  # 判断是否是响应的数据,1号控制器2001,1000位
            baojing = (lines[i + 2])[25:]  # 获取报警数据
            baojingzongshu = baojing.count("1")  # 统计报警个数
            print(baojingzongshu)




from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 140, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 180, 54, 12))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(str(baojingzongshu))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())





