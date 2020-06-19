import re,os
import tkinter
from tkinter import *

def eachFile(filepath):
    pathDir =os.listdir(filepath)        #遍历文件夹中的text
    # print(pathDir)
    return pathDir

def count_words(file_path):
    with open(file_path,'rb') as file:
        text=file.read()
        words=re.findall(','.encode('UTF-8'),text)
        #print(words)
        count=len(words)
    return count

root = Tk()
root.title('CPUTest')
root.geometry('500x200')
root.wm_attributes('-topmost', 0)
root.resizable(width=True,height=False)
t = StringVar()

def Test():
    word_sum = 0
    # filePath = "D:\\log\\log\\files\\logs\\network\\"
    filePath = Entry_road.get()
    pathDir = eachFile(filePath)
    for allDir in pathDir:
        word_sum = count_words(filePath +"\\"+ allDir) + word_sum
    print(word_sum)

t.set('D:\\log\\log\\files\\logs\\recogresult\\')

label_env = tkinter.Label(root, text="设备CPU占用率测试",borderwidth=5).grid(row=0, column=1,columnspan=4)
Entry_road = Entry(root, borderwidth=1,textvariable=t,width=40)
text_road = tkinter.Label(root, text="路径:",anchor=E,borderwidth=5).grid(row=2,column=0)
label2 = tkinter.Label(root, text="输出文件：")
labe11 = tkinter.Label(root, text="",width=2).grid(row=2,column=6)
comand = Button(root, text="获取", command=Test,width=10, height=3,relief = 'raised').grid(row=2, column = 7,columnspan=3,rowspan=3)
label2.grid(row=5, column = 0)
Entry_road.grid(row=2, column = 1,columnspan=5)

root.mainloop()

# print(count_words('D:\\log\\log\\files\\logs\\recogresult\\2019-03-27-19.txt'))