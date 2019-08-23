# -*- coding: utf-8 -*-
import xlrd
import pyautogui
# 使用时配置软件在屏幕右侧，先点击需要加点的回路

def read_excel():  # 打开文件
    workbook = xlrd.open_workbook('C:/Users/DELL/Desktop/1.xlsx')
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    luobo = 1  # luobo是循环次数
    while luobo < 125 :
        adress = sheet1.cell_value(luobo, 0)  # 只获取cell中的内容,单元格要设置为文本格式，数字前面加逗号
        zone = sheet1.cell_value(luobo, 1)  # 只获取cell中的内容，区域
        zone1 = sheet1.cell_value(luobo-1, 1)
        mold = sheet1.cell_value(luobo, 2)  # 只获取cell中的内容，类型
        mold1 = sheet1.cell_value(luobo-1, 2)  # 只获取cell中的内容，类型
        print(zone)
        print(adress)
        print(mold)
        pyautogui.PAUSE = 0.4  # 每执行一个函数后暂停0.5s
        pyautogui.FAILSAFE = True  # 触发异常，终止程序，鼠标移动到屏幕左上角
        print(pyautogui.position())  # 获取当前鼠标坐标
        pyautogui.click(1687, 63)  # button是要点击的按键，‘left'（左键也是默认）, ‘middle', ‘right'
        # 1687 63是配置软件右半边屏+点的坐标

        # 选择类型
        if mold == mold1 :
            print('爱')
        else:
            pyautogui.moveTo(1403, 167, duration=0.5)  # 移动鼠标到类型，duration为所需的时间
            pyautogui.doubleClick()  # 双击鼠标
            pyautogui.scroll(2000)  # 滚动鼠标到光纤，当值为负数时，向下滚动，125为一个单位
            rolling = 0
            if mold == 'VOA' :
                rolling = 0  # 感烟
            elif mold == 'VIRA' :
                rolling = -125  # 火焰
            elif mold == 'BMAL' :
                rolling = -250  # 手报
            elif mold == 'VTVA' :
                rolling = -375  # 感温
            elif mold == 'ATAV' :
                rolling = -750  # 输入
            elif mold == 'MBASV(' :
                rolling = -1000  # 接口模块
            else:
                pyautogui.alert('探测器类型有误，检查EXCEL')  # 这个消息弹窗是文字+OK按钮
            pyautogui.scroll(rolling)

    # 地址
        pyautogui.moveTo(1621, 167, duration=0.5)  # 移动鼠标到地址，duration为所需的时间
        pyautogui.doubleClick()  # 双击鼠标
        pyautogui.typewrite(str(adress))  # 输入地址  注意中文无法输入

    # 区域
        if rolling == -750 :  # 当类型为输入模块时
            if mold1 == mold :
                pyautogui.moveTo(1677, 290, duration=0.5)  # 移动鼠标到区域编号位置，duration为所需的时间
                pyautogui.doubleClick()  # 双击鼠标
                pyautogui.typewrite(str(zone))  # 输入区域  注意中文无法输入
            else:
                pyautogui.moveTo(1504, 290, duration=0.5)  # 移动鼠标到输入2位置，duration为所需的时间
                pyautogui.doubleClick()  # 双击鼠标
                pyautogui.scroll(600)
                pyautogui.scroll(-250)
                pyautogui.moveTo(1677, 290, duration=0.5)  # 移动鼠标到区域编号位置，duration为所需的时间
                pyautogui.doubleClick()  # 双击鼠标
                pyautogui.typewrite(str(zone))  # 输入区域  注意中文无法输入
        else:
            pyautogui.moveTo(1385, 287, duration=0.5)  # 移动鼠标到区域编号位置，duration为所需的时间
            pyautogui.doubleClick()  # 双击鼠标
            pyautogui.typewrite(str(zone))  # 输入区域  注意中文无法输入
        luobo = luobo + 1
    else:
        pyautogui.alert('完成')
    print(luobo)

if __name__ == '__main__':
    read_excel()
