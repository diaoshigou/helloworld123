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
                    NIR_list.append(int(NIR_demo))
        fopen.close()
    except Exception as e:
        print(e)
    for i in NIR_list:
        NIR_sum = NIR_sum + i
        # print(i)
    return (NIR_sum,NIR_list)

def FMP(road,FMP_list):
    global FMP_sum
    FMP_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "Magicmirror FMP" in str(lines):
                FMP_demo = lines[lines.find("cost")+11:lines.find("error count")-6]
                # print(FMP_demo)
                if (int(FMP_demo) < 1000):
                    FMP_list.append(int(FMP_demo))
        fopen.close()
    except Exception as e:
        print(e)
    for i in FMP_list:
        FMP_sum = FMP_sum + i
    return (FMP_sum,FMP_list)

def detect(road,detect_list):
    detect_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "Rgb detect cost time" in str(lines):
                detect_Demo = lines[lines.find("cost") + 12:-1]
                # print(detect_Demo)
                if (int(detect_Demo) < 2000):
                    detect_list.append(int(detect_Demo))
        fopen.close()
    except Exception as e:
        print(e)
    for i in detect_list:
        detect_sum = detect_sum + i
    return (detect_sum,detect_list)

def Recognize_offline(road,Recognize_offline_list):
    global Recognize_offline_sum
    Recognize_offline_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "RGB recognizeResult" in str(lines) and str(lines)[lines.find('name')+5:lines.find('name')+6] != ',':# 离线识别
                Recognize_offline_Demo = lines[lines.find("faceScore") + 10:lines.find("..offline")] # 离线识别

                Recognize_offline_list.append(Recognize_offline_Demo)
        fopen.close()

    except Exception as e:
        print(e)
    for i in Recognize_offline_list:
        Recognize_offline_sum = Recognize_offline_sum + float(i)
    return (Recognize_offline_sum,Recognize_offline_list)

def Recognize_online(road,Recognize_online_list):
    global Recognize_online_sum
    Recognize_online_sum = 0
    try:
        fopen = open(road,encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "RGB online recognizeResult" in str(lines): # 在线识别
                Recognize_online_Demo = lines[lines.find("cost time") + 10:lines.find("response time") - 2] # 在线识别
                Recognize_online_list.append(Recognize_online_Demo)
        fopen.close()

    except Exception as e:
        print(e)
    for i in Recognize_online_list:
        Recognize_online_sum = Recognize_online_sum + float(i)
    return (Recognize_online_sum,Recognize_online_list)

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
                    WARM_list.append(int(WARM_demo))
        fopen.close()
    except Exception as e:
        print(e)
    for i in WARM_list:
        WARM_sum = WARM_sum + i
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
                    quality_list.append(int(quality_demo))
        fopen.close()
    except Exception as e:
        print(e)
    for i in quality_list:
        quality_sum = quality_sum + i
    return (quality_sum,quality_list)



def setkind():
    k = []
    if chVarNIR.get() == int(1):
        k.append('1')
    if chVarFMP.get() == int(1):
        k.append('2')
    if chVardetect.get() == int(1):
        k.append('3')
    if chVarRecongnize_offline.get() == int(1):
        k.append('4')
    if chVarRecongnize_online.get() == int(1):
        k.append("5")
    if chVarWarm.get() == int(1):
        k.append('6')
    if chVarquality.get() == int(1):
        k.append("7")
    if chVarALL_chain.get() == int(1):
        k.append('8')

    return k

def Ttest():
    NIR_list = []
    FMP_list = []
    detect_list = []
    Recognize_offline_list = []
    Recognize_online_list = []
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
                print("未找到NIR记录")
            else:
                print("NIR耗时：" + str(round(NIR_sum / len(NIR_list),2)) + "ms（" + str(max(NIR_list)) + "ms-"+ str(min(NIR_list)) + "ms)")
        if i == '2':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (FMP_sum,FMP_list) = FMP(road,FMP_list)
            if len(FMP_list) == 0:
                print("未找到FMP记录")
            else:
                print("FMP耗时：" + str(round(FMP_sum / len(FMP_list),2)) + "ms（" + max(FMP_list) + "ms-"+ min(FMP_list) + "ms)")
        if i == '3':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (detect_sum,detect_list) = detect(road,detect_list)
            if len(detect_list) == 0:
                print("未找到detect记录")
            else:
                print("detect耗时：" + str(round(detect_sum / len(detect_list),2)) + "ms(" + str(max(detect_list)) + "ms-" + str(min(detect_list)) + "ms)")
        if i == '4':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (Recognize_offline_sum,Recognize_offline_list) = Recognize_offline(road,Recognize_offline_list)
            if len(Recognize_offline_list) == 0:
                print("未找到离线Recognize记录")
            else:
                print("Recognize耗时：" + str(round(Recognize_offline_sum / len(Recognize_offline_list),2)) + "ms(" + str(round(float(max(Recognize_offline_list)),2)) + "ms-" + str(round(float(min(Recognize_offline_list)),2)) + "ms)")
        if i == '5':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (Recognize_online_sum,Recognize_online_list) = Recognize_online(road,Recognize_online_list)
            if len(Recognize_online_list) == 0:
                print("未找到在线Recognize记录")
            else:
                print("Recognize耗时：" + str(round(Recognize_online_sum / len(Recognize_online_list),2)) + "ms(" + str(round(float(max(Recognize_online_list)),2)) + "ms-" + str(round(float(min(Recognize_online_list)),2)) + "ms)")
        if i == '6':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (Warm_sum,Warm_list) = WARM(road,Warm_list)
            if len(Warm_list) == 0:
                print("未找到Warm记录")
            else:
                print("Warm平均时间：" + str(round(Warm_sum / len(Warm_list),2)) + "ms(" + str(max(Warm_list)) + "ms-" + str(min(Warm_list)) + "ms)")
        if i == '7':
            for allDir in pathDir:
                road = Entry_road.get() + '\\' + allDir
                (quality_sum,quality_list) = quality(road,quality_list)
            if len(quality_list) == 0:
                print("未找到quality记录")
            else:
                print("quality平均时间：" + str(round(quality_sum / len(quality_list),2)) + "ms(" + str(max(quality_list)) + "ms-" + str(min(quality_list)) + "ms)")
        if i == '8':
            if "4" in k:
                if len(Recognize_offline_list) != 0:
                    ALL_Time_ave_offline = round(NIR_sum / len(NIR_list),2) + round(detect_sum / len(detect_list),2) + round(Recognize_offline_sum / len(Recognize_offline_list),2) + round(Warm_sum / len(Warm_list),2) + round(quality_sum / len(quality_list),2)
                    ALL_Time_max_offline = float(max(NIR_list)) + float(max(detect_list)) + round(float(max(Recognize_offline_list)),2) + float(max(Warm_list)) + float(max(quality_list))
                    ALL_Time_min_offline = float(min(NIR_list)) + float(min(detect_list)) + round(float(min(Recognize_offline_list)),2) + float(min(Warm_list)) + float(min(quality_list))
                    print("离线全链路耗时：" + str(round(ALL_Time_ave_offline,2)) + "ms(" + str(round(ALL_Time_max_offline,2)) + "ms-" + str(round(ALL_Time_min_offline,2)) + "ms)")
                else:
                    print("无离线识别记录！")
            if "5" in k:
                if len(Recognize_online_list) != 0:
                    ALL_Time_ave = round(NIR_sum / len(NIR_list), 2) + round(detect_sum / len(detect_list), 2) + round(
                        Recognize_online_sum / len(Recognize_online_list), 2) + round(Warm_sum / len(Warm_list),
                                                                                        2) + round(
                        quality_sum / len(quality_list), 2)
                    print("在线全链路耗时：" + str(round(ALL_Time_ave, 2)) + "ms")
                else:
                    print("无在线识别记录！")



root = Tk()
root.title('CPUTest')
root.geometry('500x200')
root.wm_attributes('-topmost', 0)
root.resizable(width=True,height=False)
t = StringVar()

chVarNIR = tkinter.IntVar()   # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0
chVarFMP = tkinter.IntVar()
chVardetect = tkinter.IntVar()
chVarRecongnize_offline = tkinter.IntVar()
chVarWarm = tkinter.IntVar()
chVarquality = tkinter.IntVar()
chVarRecongnize_online = tkinter.IntVar()
chVarALL_chain = tkinter.IntVar()

t.set(r'C:\Users\86183\Desktop\logs\logs\D2PLUS')


label_env = tkinter.Label(root, text="设备CPU占用率测试",borderwidth=5).grid(row=0, column=1,columnspan=4)
Entry_road = Entry(root, borderwidth=1,textvariable=t,width=40)
text_road = tkinter.Label(root, text="路径:",anchor=E,borderwidth=5).grid(row=2,column=0)
label2 = tkinter.Label(root, text="")
# labe11 = tkinter.Label(root, text="",width=2).grid(row=2,column=6)
comand = Button(root, text="获取", command=Ttest,width=10, height=3,relief = 'raised').grid(row=2, column = 7,columnspan=3,rowspan=3)
label2.grid(row=5, column = 0)
Entry_road.grid(row=2, column = 1,columnspan=5)

# 复选框
check1 = tkinter.Checkbutton(root, text="NIR", variable=chVarNIR)    # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
check1.select()     # 该复选框是否勾选,select为勾选, deselect为不勾选
check1.grid(column=0, row=14, sticky=tkinter.W)
check2 = tkinter.Checkbutton(root, text="FMP", variable=chVarFMP)
check2.grid(column=1, row=14, sticky=tkinter.W)
check2.select()
check3 = tkinter.Checkbutton(root, text="detect", variable=chVardetect)
check3.grid(column=2, row=14, sticky=tkinter.W)
check3.select()
check4 = tkinter.Checkbutton(root, text="Recongnize_offline", variable=chVarRecongnize_offline)
check4.grid(column=3, row=14, sticky=tkinter.W)
check4.select()
check5 = tkinter.Checkbutton(root, text="Recognize_online", variable=chVarRecongnize_online)
check5.grid(column=3, row=15, sticky=tkinter.W)
check5.select()
check6 = tkinter.Checkbutton(root, text="WARM", variable=chVarWarm)
check6.grid(column=0, row=15, sticky=tkinter.W)
check6.select()
check7 = tkinter.Checkbutton(root, text="quality", variable=chVarquality)
check7.grid(column=1, row=15, sticky=tkinter.W)
check7.select()
check8 = tkinter.Checkbutton(root, text="ALL_chain", variable=chVarALL_chain)
check8.grid(column=2, row=15, sticky=tkinter.W)
check8.select()
root.mainloop()
