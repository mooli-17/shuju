# -*- coding: utf-8 -*-

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import logging
from logging.handlers import TimedRotatingFileHandler
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from ui_1 import Ui_MainWindow  # 从QT Desinger生成的文件中调用  from文件的名称，import 文件中的Class类的名称
import sys
import threading
import time

# author : luobo（2422973253@qq.com)
# date : 11.08.2019


class modbus_485(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(modbus_485, self).__init__()
        self.setupUi(self)
        self.sent_data()

    def data(self):
        # ---设置485主从站----
        # 设定串口为从站
        PORT = "com1"  # 串口号
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))  # 串口设置
        master.set_timeout(10.0)  # 通信失败延时时间
        master.set_verbose(True)  # 设置debug的log输出

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
        while True:
            logger = modbus_tk.utils.create_logger("console")
            logger.info("connected")
            # 01数据 1站号 地址2001 长度1000的数据
            logger.info(master.execute(1, cst.READ_COILS, 2001, 1000))
            time.sleep(0.5)  # 延时0.5s

            # ----处理485数据----
            with open('luoborizhi')as file_object:
                lines = file_object.readlines()  # 逐行读文件，存到表lines中
                n = len(lines)  # 获取表的长度
            for i in range(n):
                lines[i] = (lines[i])[24:50]  # 截取表第24项到末尾，保存到表
                if lines[i] == '-> 1-1-7-209-3-232-109-249' and (lines[i + 2])[24:25] == '(':  # 判断是否是响应的数据,1号控制器2001,1000位
                    baojing = (lines[i + 2])[25:]  # 获取报警数据
                    baojingzongshu = baojing.count("1")  # 统计报警个数
                    self.label_2.setText(str(baojingzongshu))
                else:
                    pass

    def sent_data(self):
        t = threading.Thread(target=self.data)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = modbus_485()
    myshow.show()
    sys.exit(app.exec_())








