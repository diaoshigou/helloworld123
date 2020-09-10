# NIR/RGB/Recognizetime
import datetime
from time import sleep
from tkinter import *
import tkinter
import os

# road = "D:\log\log\2019-03-12-17.txt"
def eachFile(filepath):
    pathDir =os.listdir(filepath)        #遍历文件夹中的text
    # print(pathDir)
    return pathDir



def NIR(road,NIR_list):
    global NIR_sum
    NIR_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "NIR cost time" in str(lines):
            # if "Magicmirror FMP" in str(lines):
                NIR_demo = lines[lines.find("cost")+11:lines.find("error count")-6]
                # print(NIR_demo)
                if (int(NIR_demo) < 1000):
                    NIR_list.append(NIR_demo)
        fopen.close()
    except Exception as e:
        print(e)
    for i in NIR_list:
        NIR_sum = NIR_sum + int(i)
    return (NIR_sum,NIR_list)

def detect(road,detect_list):
    detect_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "Rgb detect cost time" in str(lines):
                detect_Demo = lines[lines.find("cost") + 12:-1]
                # print(detect_Demo)
                if (int(detect_Demo) < 2000):
                    detect_list.append(detect_Demo)
        fopen.close()
    except Exception as e:
        print(e)
    for i in detect_list:
        detect_sum = detect_sum + int(i)
    return (detect_sum,detect_list)

def Recognize(road,Recognize_list):
    global Recognize_sum
    Recognize_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "RGB recognizeResult" in str(lines) and str(lines)[lines.find('name')+5:lines.find('name')+6] != ',':
            # if "RGB online recognizeResult" in str(lines):
            #     Recognize_Demo = lines[lines.find("cost time") + 10:lines.find("response time") - 2]
                Recognize_Demo = lines[lines.find("faceScore") + 10:lines.find("..offline")]
                print(Recognize_Demo)
                # if(int(Recognize_Demo) < 2000):
                    # print(Recognize_Demo)
                Recognize_list.append(Recognize_Demo)
        fopen.close()

    except Exception as e:
        print(e)
    for i in Recognize_list:
        Recognize_sum = Recognize_sum + float(i)
    return (Recognize_sum,Recognize_list)

def WARM(road,WARM_list):
    global WARM_sum
    WARM_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "warmUp" in str(lines):
            # if "Magicmirror FMP" in str(lines):
                WARM_demo = lines[lines.find("cost")+10:-1]
                # print(NIR_demo)
                if (int(WARM_demo) < 1000):
                    WARM_list.append(WARM_demo)
        fopen.close()
    except Exception as e:
        print(e)
    for i in WARM_list:
        WARM_sum = WARM_sum + int(i)
    return (WARM_sum,WARM_list)

def quality(road,quality_list):
    global quality_sum
    quality_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "quality cost time" in str(lines):
            # if "Magicmirror FMP" in str(lines):
                quality_demo = lines[lines.find("cost")+10:-1]
                # print(quality_demo)
                if (int(quality_demo) < 1000):
                    quality_list.append(quality_demo)
        fopen.close()
    except Exception as e:
        print(e)
    for i in quality_list:
        quality_sum = quality_sum + int(i)
    return (quality_sum,quality_list)



def setkind():
    k = []
    if chVarNIR.get() == int(1):
        k.append('1')
    if chVardetect.get() == int(1):
        k.append('2')
    if chVarRecongnize.get() == int(1):
        k.append('3')
    if chVarWarm.get() == int(1):
        k.append('4')
    if chVarquality.get() == int(1):
        k.append("5")

    return k

def Ttest():
    NIR_list = []
    detect_list = []
    Recognize_list = []
    Warm_list = []
    quality_list = []
    filePath = Entry_road.get()
    pathDir = eachFile(filePath)
    k = setkind()
    for i in k:
        if i == '1':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (NIR_sum,NIR_list) = NIR(road,NIR_list)
            if len(NIR_list) == 0:
                print("未找到NIR/fmp记录")
            else:
                print("NIR平均时间：" + str(NIR_sum / len(NIR_list)))
        if i == '2':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (detect_sum,detect_list) = detect(road,detect_list)
            if len(detect_list) == 0:
                print("未找到detect记录")
            else:
                print("detect平均时间：" + str(detect_sum / len(detect_list)))
        if i == '3':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (Recognize_sum,Recognize_list) = Recognize(road,Recognize_list)
            if len(Recognize_list) == 0:
                print("未找到Recognize记录")
            else:
                print("Recognize平均时间：" + str(Recognize_sum / len(Recognize_list)))
        if i == '4':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (Warm_sum,Warm_list) = WARM(road,Warm_list)
            if len(Warm_list) == 0:
                print("未找到Warm记录")
            else:
                print("Warm平均时间：" + str(Warm_sum / len(Warm_list)))
        if i == '5':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (quality_sum,quality_list) = quality(road,quality_list)
            if len(quality_list) == 0:
                print("未找到quality记录")
            else:
                print("quality平均时间：" + str(quality_sum / len(quality_list)))

    # print("NIR/fmp平均时间：" + str(NIR_sum / len(NIR_list)))

    # print("Recongnize平均时间：" + str(Recognize_sum / len(Recognize_list)))


root = Tk()
root.title('CPUTest')
root.geometry('500x200')
root.wm_attributes('-topmost', 0)
root.resizable(width=True,height=False)
t = StringVar()

chVarNIR = tkinter.IntVar()   # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0
chVardetect = tkinter.IntVar()
chVarRecongnize = tkinter.IntVar()
chVarWarm = tkinter.IntVar()
chVarquality = tkinter.IntVar()
t.set(r'C:\Users\86183\Desktop\pause\D3')


label_env = tkinter.Label(root, text="设备CPU占用率测试",borderwidth=5).grid(row=0, column=1,columnspan=4)
Entry_road = Entry(root, borderwidth=1,textvariable=t,width=40)
text_road = tkinter.Label(root, text="路径:",anchor=E,borderwidth=5).grid(row=2,column=0)
label2 = tkinter.Label(root, text="输出文件：")
labe11 = tkinter.Label(root, text="",width=2).grid(row=2,column=6)
comand = Button(root, text="获取", command=Ttest,width=10, height=3,relief = 'raised').grid(row=2, column = 7,columnspan=3,rowspan=3)
label2.grid(row=5, column = 0)
Entry_road.grid(row=2, column = 1,columnspan=5)

# 复选框
check1 = tkinter.Checkbutton(root, text="NIR", variable=chVarNIR)    # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
check1.select()     # 该复选框是否勾选,select为勾选, deselect为不勾选
check1.grid(column=0, row=14, sticky=tkinter.W)
check2 = tkinter.Checkbutton(root, text="detect", variable=chVardetect)
check2.grid(column=1, row=14, sticky=tkinter.W)
check2.select()
check3 = tkinter.Checkbutton(root, text="Recongnize", variable=chVarRecongnize)
check3.grid(column=2, row=14, sticky=tkinter.W)
check3.select()

check4 = tkinter.Checkbutton(root, text="WARM", variable=chVarWarm)
check4.grid(column=3, row=14, sticky=tkinter.W)
check4.select()
check5 = tkinter.Checkbutton(root, text="quality", variable=chVarquality)
check5.grid(column=4, row=14, sticky=tkinter.W)
check5.select()

root.mainloop()
