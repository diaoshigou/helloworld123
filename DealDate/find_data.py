import os
from tkinter import *
import tkinter

# 遍历文件夹中的text
def eachFile(filepath):
    try:
        pathDir =os.listdir(filepath)
        return pathDir
    except Exception as e:
        lb.insert(END,"文件路径错误：" + str(e)[str(e).find("]")+2:str(e).find("。")])

# 检测是否存在数据文件夹，若存在则删除(覆盖写入)
def Detect(Path_D):
    if os.path.exists(Path_D + "\\data.txt") == True:
        os.remove(Path_D + "\\data.txt")
    else:
        pass

# 检测每行是否有关键字，若有则显示
def readfile(name,sum):
    fopen=open(name,'rb')
    word = keyword.get()

    for lines in fopen.readlines():         #按行读取text中的内容
        liness=lines.decode(encoding = "utf-8")
        # liness = liness.replace("\n", "").split(",")
        if word in str(liness):
            sum.append(str(liness))
    fopen.close()
    return sum

def finddata():
    lb.delete(0, END)
    Path_D = entry_dealfile.get()
    if IC.get() == '1': # 若"覆盖"选中则删除原文件
        Detect(Path_D)
    path = filepath.get()
    filePath = path
    pathDir = eachFile(filePath)
    sum = []
    try:
        for allDir in pathDir:
            child = filePath + '\\' + allDir
            readfile(child,sum)
        try:
            if dealfile_path.get() == '1':  # 如果保存文件被选择
                with open(Path_D + "\\data.txt", 'a+') as f:
                    for i in sum:
                        if len(i) > 700:
                            lb.insert(END, str(i)[:500] + "..........................." + str(i)[-200:])
                        else:
                            lb.insert(END,str(i))
                        if str(i)[-1:] == '\n':
                            f.write(str(i))
                        else:
                            f.write(str(i)+'\n')
                    lb.insert(0, "出现次数：" + str(len(sum)))
                    lb.insert(0, "数据筛选完成！")
            else:
                for i in sum:
                    if len(i) > 700:
                        lb.insert(END, str(i)[:500] + "..........................." + str(i)[-200:])
                    else:
                        lb.insert(END, str(i))
                lb.insert(0, "出现次数：" + str(len(sum)))
                lb.insert(0, "数据筛选完成！")
        except Exception as e:
            lb.insert(END,e)
    except Exception as e:
        lb.insert(END,e)


root = Tk()
root.title("SelectData")
root.geometry('950x350') # 全局界面大小
root.wm_attributes('-topmost', 1) # 永远保持最前
keyword = StringVar()   # 筛选关键字
# keyword.set('ding')
filepath = StringVar()  # 需要被筛选的文件路径
# filepath.set(r'C:\Users\86183\Desktop\pause\log\090202190702KN0113\measureTemperature')
sb = Scrollbar(root)    #垂直滑动条
sbx =Scrollbar(root,orient='horizontal')    # 水平滑动条
entry_dealfile = StringVar() #
# entry_dealfile.set(r'C:\Users\86183\Desktop\pause\log')
listbox = StringVar()
dealfile_path = StringVar() # 统计文件路径
dealfile_path.set(0)
IC = StringVar()    # 覆盖选项
IC.set(0)


Space = tkinter.Label(root,text="",borderwidth=0,width=1).grid(row=0,column=0)
Keyword = tkinter.Label(root,text="关键词：",borderwidth=5,width=15,anchor=NE).grid(row=1,column=2)
Entry_Keyword = Entry(root, borderwidth=1,textvariable=keyword,width=20).grid(row=1,column=3,sticky=W)

Data_FilePath = tkinter.Label(root,text="文件路径：",borderwidth=5,width=15,anchor=NE).grid(row=2,column=2)
Entry_FilePath = Entry(root, borderwidth=1,textvariable=filepath,width=40).grid(row=2,column=3,columnspan=2)

DealFile_Path = tkinter.Checkbutton(root,text="生成数据路径：",variable = dealfile_path,borderwidth=5,width=15,anchor=NE).grid(row=3,column=2)
Entry_DealFile = Entry(root, borderwidth=1,textvariable=entry_dealfile,width=40).grid(row=3,column=3,columnspan=2)

comand = Button(root, text="获取", command=finddata,width=10, height=2,borderwidth=2).grid(row=2, column=6,rowspan=3,sticky=W)

IfCover = tkinter.Checkbutton(root,text="覆盖",variable = IC,borderwidth=5,width=5,anchor=W).grid(row=3,column=5)

lb = Listbox(root,yscrollcommand= sb.set,xscrollcommand=sbx.set,width=60,listvariable=listbox,selectmode='extended')

sb.grid(row=5, column=10,sticky='ENS',rowspan=5)
sbx.grid(row=10,column=3,columnspan=7,sticky='SWE')

lb.grid(row=5,sticky='W', column=3,rowspan=5,columnspan=7,ipadx=100)

sb.config(command=lb.yview)
sbx.config(command=lb.xview)
root.mainloop()