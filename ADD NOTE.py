# -*- coding: utf-8 -*-
import xlrd
import win32con
import win32clipboard as w
import pyautogui

workbook = xlrd.open_workbook('C:/Users/DELL/Desktop/1.xlsx')
sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
luobo = 1  # luobo是循环次数
while luobo < 201:
    note = sheet1.cell_value(luobo, 0)  # 只获取cell中的内容,单元格要设置为文本格式，数字前面加逗号
    print(note)
    w.OpenClipboard()  # 打开剪切板
    w.SetClipboardData(win32con.CF_UNICODETEXT, note)  # 写入剪切板
    w.CloseClipboard()  # 关闭剪切板

    pyautogui.PAUSE = 0.5  # 每执行一个函数后暂停0.5s
    pyautogui.FAILSAFE = True  # 触发异常，终止程序，鼠标移动到屏幕左上角
    print(pyautogui.position())  # 获取当前鼠标坐标
    # 移动鼠标到编辑按钮
    pyautogui.click(1664, 63, duration=0.5)  # button是要点击的按键，‘left'（左键也是默认）, ‘middle', ‘right'
    # 移动到点标签的位置
    pyautogui.click(1784, 237)  # button是要点击的按键，‘left'（左键也是默认）, ‘middle', ‘right'
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite(['enter'])
    pyautogui.click(1300, 512, duration=0.8)  # 移动到左边点列表的空白的地方
    pyautogui.typewrite(['down'])
    luobo = luobo + 1
else:
    print('完成')
