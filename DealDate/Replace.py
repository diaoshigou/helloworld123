import os
# from time import sleep
from tkinter import *
import tkinter
i = 0
def eachFile(filepath):
    try:
        pathDir =os.listdir(filepath)        #遍历文件夹中的text
        return pathDir
    except Exception as e:
        # tips['text'] = "文件路径错误：" + str(e)[str(e).find("]")+2:str(e).find("。")]
        lb.insert(END,"文件路径错误：" + str(e)[str(e).find("]")+2:str(e).find("。")])

def Detect(Path_D):
    global i
    i=i+1
    if os.path.exists(Path_D + "\\data.txt") == True:
        os.remove(Path_D + "\\data.txt")
    else:
        pass


def readfile(name):
    fopen=open(name,'r')
    word = K.get()
    Path_D = D.get()
    sum=[]
    count = 8001
    for lines in fopen.readlines():         #按行读取text中的内容
        if '1634870006946725888' in str(lines):
            # print("1")
            # print(str(lines)[str(lines).find('VALUES')+8:str(lines).find('1634870006946725888')-2])
            liness = str(lines)[:str(lines).find('VALUES')+8] + str(count) +str(lines)[str(lines).find('1634870006946725888')-2:]
            # print(liness)

            sum.append(str(liness))
            count += 1

    fopen.close()
    # print("1")
    try:
        with open(Path_D + "\\data.txt", 'a+') as f:
            for i in sum:
                # lb.insert(END,str(i))
                f.write(str(i))
                # print(i)
                # pass
        return 'corrent'
    except Exception as e:
        # words_error = str(e)
        if str(V.get())[3:10] != 'Errno 2' and '生成数据路径错误！' not in str(V.get()) :
            lb.insert(END,"生成数据路径错误！")
        else:
            pass
        return 'error'



def finddata():
    lb.delete(0, END)
    Path_D = D.get()
    Detect(Path_D)
    path = P.get()
    filePath = path
    pathDir = eachFile(filePath)
    try:
        count = 0
        for allDir in pathDir:
            child = filePath + '\\' + allDir
            count = readfile(child)
    except Exception as e:
        # lb.insert(END,e)
        pass
    finally:
        if count == 'corrent':
            lb.insert(END,'筛选数据完成！')
        else:
            pass
            # lb.insert(END,'2')


root = Tk()
root.title("SelectData")
root.geometry('900x400')
# root.wm_attributes('-topmost', 1)
K = StringVar()
K.set(r"atm")
P = StringVar()
P.set(r"C:\Users\admin\Desktop\pause\2")
D = StringVar()
sb = Scrollbar(root)
pwd = os.getcwd()
D.set(pwd)
V = StringVar()

Space = tkinter.Label(root,text="",borderwidth=0,width=1).grid(row=0,column=0)
Keyword = tkinter.Label(root,text="关键词：",borderwidth=0,width=15,anchor=NE).grid(row=1,column=2)
Entry_Keyword = Entry(root, borderwidth=1,textvariable=K,width=20).grid(row=1,column=3)

Space2 = tkinter.Label(root,text="",borderwidth=0,width=20).grid(row=1,column=4)

Data_FilePath = tkinter.Label(root,text="文件路径：",borderwidth=5,width=15,anchor=NE).grid(row=2,column=2)
Entry_FilePath = Entry(root, borderwidth=1,textvariable=P,width=40).grid(row=2,column=3,columnspan=2)

DealFile_Path = tkinter.Label(root,text="生成数据路径：",borderwidth=5,width=15,anchor=NE).grid(row=3,column=2)
Entry_DealFile = Entry(root, borderwidth=1,textvariable=D,width=40).grid(row=3,column=3,columnspan=2)

Space3 = tkinter.Label(root,text="",borderwidth=0,width=1).grid(row=2,column=5)
comand = Button(root, text="获取", command=finddata,width=10, height=2,borderwidth=2).grid(row=2, column=6,rowspan=2)
Sapce4 = tkinter.Label(root,text="",width=50).grid(row=3,column=7)
Sapce5 = tkinter.Label(root,text="",width=50).grid(row=3,column=8)

# tips = tkinter.Label(root,text="您好",borderwidth=0,width=10,anchor=NW)
#
# tips.grid(row=5,column=0,columnspan=50)

lb = Listbox(root,yscrollcommand= sb.set,width=104,listvariable=V,selectmode='extended')
sb.grid(row=4, column=8,sticky='WNS',rowspan=5)
# for i in range(20):
#     lb.insert(END,i)
lb.grid(row=4,sticky='WNS', column=3,rowspan=5,columnspan=50)

sb.config(command=lb.yview)
root.mainloop()