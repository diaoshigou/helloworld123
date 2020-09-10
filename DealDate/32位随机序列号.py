import tkinter
from random import *
from tkinter import *


def MAC():
    m = n_number.get()
    mac = 3*int(m)+1
    for number in range(1,mac):
        list=[]
        for n in range(1,13):
            a = hex(randrange(1,16))
            if a.startswith('0x'): #不必要
                a = a[2:]
                list.append(a)
        list2 = ''.join(list)
        print(list2)
        # print(mac)
        # print(type(int(a-1)/3))

        if number%3 == 0:
            SecretKey(m)

def SecretKey(s):
    for number in range(1,int(s)+1):
        list=[]
        for n in range(1,33):
            a = hex(randrange(1,16))
            if a.startswith('0x'): #不必要
                a = a[2:]
                list.append(a)
        list2 = ''.join(list)
        print(list2)

# def Creat():


root = Tk()
root.title("SelectData")
root.geometry('375x275')
# root.wm_attributes('-topmost', 1)

canvas=Canvas(root,width=350,height=250,scrollregion=(0,0,200,275)) #创建canvas：参数显示容器
canvas.place(x = 10, y = 10) #放置canvas的位置
frm=tkinter.Frame(canvas)
frm.place(x = 10, y = 10)

MAC_add = IntVar()
MAC_add.set(1)
SecKey_add = IntVar()
SecKey_add.set(1)
n_number = StringVar()

Button_CreateMac = tkinter.Checkbutton(frm,text="1、创建MAC地址：",variable=MAC_add).grid(row=0 ,column=0,sticky=tkinter.W)
Button_CreateSecKey = tkinter.Checkbutton(frm,text="1、创建秘钥：",variable=SecKey_add).grid(row=1 ,column=0,sticky=tkinter.W)
Lable_number = tkinter.Label(frm,text="创建组数：").grid(row=2,column=0,sticky=tkinter.W)
Entry_number = tkinter.Entry(frm,textvariable = n_number).grid(row=2,column=1,sticky=tkinter.W)

comand = Button(root, text="获取", command=MAC, width=10, height=2).place(x=50,y=120)

scr1 = Scrollbar(root)
scr1['command']=canvas.yview

root.mainloop()