import os
import xlwt
from tkinter import *
import tkinter
import tkinter as tk

master = Tk()
# var = IntVar()
workbook = xlwt.Workbook(encoding = 'ascii')

def eachFile(filepath):
    pathDir =os.listdir(filepath)        #遍历文件夹中的text
    return pathDir

trackId_collection=[]
trackId_NIR=[]
trackId_RGB=[]
J = 0   #sheet表序号
n = 0   #excel表格行号

def readfile(name):
    global J
    global n

    #筛选文件中trackId
    fopen=open(name,'rb')
    for lines in fopen.readlines():
        lines=lines.decode(encoding = "utf-8")
        lines = lines.replace("\n", "").split(",")
        if 'trackId' in str(lines):
            lines = str(lines)
            if lines[lines.find('trackId'):lines.find('preview')-5] not in trackId_collection:
                trackId_collection.append(lines[lines.find('trackId'):lines.find('preview')-5])
        continue
    fopen.close()

    worksheet = workbook.add_sheet('My Worksheet' + str(J))     #新建sheet表
    for i in trackId_collection:    #逐个trackId查找
        fopen = open(name, 'rb')
        # print(i)
        for lines in fopen.readlines():  # 按行读取text中的内容
            lines = lines.decode(encoding="utf-8")
            lines = lines.replace("\n", "").split(",")
            lines = str(lines)

            if ' '+i in lines and 'NIR' in lines:       #查找该trackId NIR记录
                NIR_info = lines[lines.find('trackId'):lines.find('preview')-5]+','+\
                      lines[lines.find('reuslt'):lines.find('trackId')-5]+','+\
                      lines[lines.find('cost'):-2]
                trackId_NIR.append(NIR_info)   #该trackId NIR记录集合

            elif ' '+i in lines and 'RGB' in lines and 'userTag' not in lines:  #查找特征值V3版本，该trackId RGB记录
                RGB_info = lines[lines.find('trackId'):lines.find('preview')-5]+','+\
                      lines[lines.find('name'):lines.find('faceScore')-5]+','+\
                      lines[lines.find('userId'):lines.find('trackId')-5]+','+\
                      lines[lines.find('cost'):lines.find('name')-5]+','+\
                      lines[lines.find('..')+2:-2]+','+lines[2:lines.find('Magicmirror')-1]
                trackId_RGB.append(RGB_info)   #该trackId RGB记录集合

            elif ' '+i in lines and 'RGB' in lines and 'userTag' in lines:      #查找特征值V4版本，该trackId RGB记录
                RGB_info = lines[lines.find('trackId'):lines.find('preview')-5]+','+\
                      lines[lines.find('name'):lines.find('faceScore')-5]+','+\
                      lines[lines.find('userId'):lines.find('trackId')-5]+','+\
                      lines[lines.find('cost'):lines.find('userTag')-5]+','+\
                      lines[lines.find('..')+2:-2]+','+lines[2:lines.find('Magicmirror')-1]
                trackId_RGB.append(RGB_info)       #该trackId RGB 记录集合

        for i in trackId_NIR:
            print(i)
            worksheet.write(n, 0, label=i)
            n=n+1
        for i in trackId_RGB:
            print(i)
            worksheet.write(n, 0, label=i)
            n=n+1
        trackId_RGB.clear()
        trackId_NIR.clear()

    fopen.close()
    J = J + 1   #另起一张sheet表
    n = 0       #sheet表格行号清零

def hello():
    if text.get() != '' and text1.get() != '':
        name = text.get()   # 获取输入的内容
        path = text1.get()
        filePath = name
        pathDir = eachFile(filePath)
        for allDir in pathDir:
            child = name + '\\' + allDir
            readfile(child)
            workbook.save(path+'\\'+'Excel_Workbook.xls')
        label['text'] = '筛选完成，请关闭弹窗！'
    elif text.get() == '' and text1.get() != '':
        label['text'] = '请输入原始数据地址！'
    elif text.get() != '' and text1.get() == '':
        label['text'] = '请输入结果文件保存地址！'
    elif text.get() == '' and text1.get() == '':
        label['text'] = '请输入路径！'
#布局
Label(master, text="原始数据地址：").grid(row=0, column=0)
Label(master, text="输出文件保存地址：").grid(row=1, column=0)
text = tk.Entry(master, borderwidth=1, width=60).grid(row=0, column=1, columnspan=4)
text1 = tk.Entry(master, borderwidth=1, width=60).grid(row=1, column=1, columnspan=4)
label = tkinter.Label(master, text="您好",width=25).grid(row=2,column=0)
button1 = tk.Button(master, text="获取", command=hello, width=8).grid(row=2, column=2)


mainloop()  # 主消息循环