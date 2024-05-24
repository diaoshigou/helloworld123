import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from tkinter import *
import tkinter
import sys



def PLT_CPU(Date,CPU_radio_list):
    tick_spacing = (len(Date) / 8)
    try:
        if len(CPU_radio_list) != len(Date):
            Free_RAM_list = CPU_radio_list[:int(min(len(CPU_radio_list), len(Date)))]
            Date = Date[:int(min(len(Free_RAM_list), len(Date)))]
        fig, ax_CPU = plt.subplots(1, 1)
        ax_CPU.plot(Date, CPU_radio_list)
        ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        plt.title("CPU_ALL", loc="center")
        plt.xlabel('Time', fontsize=12)
        plt.ylabel("%", fontsize=12, rotation=0, labelpad=10)
        plt.xticks(rotation=45, fontsize=8)
        plt.subplots_adjust(bottom=0.26)
        plt.show()
    except ValueError:
        print("未找到可处理数据")
        sys.exit()

def PLT_MEM(Date,Free_RAM_list):
    tick_spacing = (len(Date) / 8)
    if len(Free_RAM_list) != len(Date):
        Free_RAM_list = Free_RAM_list[:int(min(len(Free_RAM_list), len(Date)))]
        Date = Date[:int(min(len(Free_RAM_list), len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Free_RAM_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Free_RAM", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("KB", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45, fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

def PLT_APK_CPU(Date,apk_cpu_radio_list):
    tick_spacing = (len(Date) / 8)
    if len(apk_cpu_radio_list) != len(Date):
        apk_cpu_radio_list = apk_cpu_radio_list[:int(min(len(apk_cpu_radio_list), len(Date)))]
        Date = Date[:int(min(len(apk_cpu_radio_list), len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, apk_cpu_radio_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_CPU", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("%", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45, fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

def PLT_APK_MEM(Date,apk_RAM_list):
    tick_spacing = (len(Date) / 8)
    if len(apk_RAM_list) != len(Date):
        apk_RAM_list = apk_RAM_list[:int(min(len(apk_RAM_list), len(Date)))]
        Date = Date[:int(min(len(apk_RAM_list), len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, apk_RAM_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_MEM", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("KB", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45, fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

def PLT_CPU_TEMP(Date,Temp_list):
    tick_spacing = (len(Date) / 8)
    if len(Temp_list) != len(Date):
        Temp_list = Temp_list[:int(min(len(Temp_list), len(Date)))]
        Date = Date[:int(min(len(Temp_list), len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Temp_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_TEMP", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("℃", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45, fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

def PLT_Argus_PID(Date,Pid_list):
    tick_spacing = (len(Date) / 8)
    if len(Pid_list) != len(Date):
        Pid_list = Pid_list[:int(min(len(Pid_list), len(Date)))]
        Date = Date[:int(min(len(Pid_list), len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Pid_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Argus_PID", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("pid", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45, fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()


def D2P(path,files,CPU_Date,Free_Date,APK_CPU_Date,APK_MEM_Date,CPU_TEMP_Date,Argus_PID_Date,CPU_radio_list,Free_RAM_list,apk_cpu_radio_list,apk_RAM_list,Temp_list,Pid_list):

    CPU_current_type = MEM_current_type = APK_CPU_current_type = APK_MEM_current_type = CPU_TEMP_current_type = Argus_PID_current_type = None

    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            try:
                if "600%cpu" in str(lines):  # CPU_ALL
                    CPU_item_type = "data"
                    if CPU_current_type == "time":
                        CPU_current_type = CPU_item_type
                        CPU_radio = (int(lines[lines.find("sys") + 4:lines.find("idle") - 1]))  # CPU_ALL
                        CPU_radio_list.append(float(CPU_radio) / 6)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    CPU_item_type = "time"
                    if CPU_current_type == None or CPU_current_type != "time":
                        CPU_current_type = CPU_item_type
                        System_time = lines[:19]
                        CPU_Date.append(System_time)

                if "Free RAM" in str(lines):  # MEM_ALL
                    MEM_item_type = "data"
                    if MEM_current_type == "time":
                        MEM_current_type = MEM_item_type
                        Free_RAM = int(str(lines[lines.find("RAM:") + 7:lines.find(",")]) + str(
                            lines[lines.find(",") + 1:lines.find("K")]))
                        Free_RAM_list.append(int(Free_RAM))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    MEM_item_type = "time"
                    if MEM_current_type == None or MEM_current_type != "time":
                        MEM_current_type = MEM_item_type
                        System_time = lines[:19]
                        Free_Date.append(System_time)

                if "u0_a" in str(lines) and "com.moredian.entrance.guard" in str(
                        lines) and "S" in lines and "channel" not in lines:  # APK_CPU
                    APK_CPU_item_type = "data"
                    if APK_CPU_current_type == "time":
                        APK_CPU_current_type = APK_CPU_item_type
                        apk_cpu_radio = float(lines[lines.find("S") + 2:lines.find("S") + 6])
                        apk_cpu_radio_list.append(int(apk_cpu_radio)/6)
                if "u0_a" in str(lines) and "com.moredian.entrance.guard" in str(
                        lines) and "R" in lines and "channel" not in lines:  # APK_CPU
                    APK_CPU_item_type = "data"
                    if APK_CPU_current_type == "time":
                        APK_CPU_current_type = APK_CPU_item_type
                        apk_cpu_radio = float(lines[lines.find("R") + 2:lines.find("R") + 6])
                        apk_cpu_radio_list.append(int(apk_cpu_radio)/6)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    APK_CPU_item_type = "time"
                    if APK_CPU_current_type == None or APK_CPU_current_type != "time":
                        APK_CPU_current_type = APK_CPU_item_type
                        System_time = lines[:19]
                        APK_CPU_Date.append(System_time)

                if "moredianMem" in str(lines):  # APK_MEM
                    APK_MEM_item_type = "data"
                    if APK_MEM_current_type == "time":
                        APK_MEM_current_type = APK_MEM_item_type
                        apk_RAM = int(str(lines[lines.find(":") + 1:lines.find(",")]) + str(
                            lines[lines.find(",") + 1:lines.find("K")]))  # APK_MEM
                        apk_RAM_list.append(int(apk_RAM))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    APK_MEM_item_type = "time"
                    if APK_MEM_current_type == None or APK_MEM_current_type != "time":
                        APK_MEM_current_type = APK_MEM_item_type
                        System_time = lines[:19]
                        APK_MEM_Date.append(System_time)

                if "getTempResult" in str(lines):  # CPU_TEMP
                    CPU_TEMP_item_type = "data"
                    if CPU_TEMP_current_type == "time":
                        CPU_TEMP_current_type = CPU_TEMP_item_type
                        Temp = lines[lines.find("|") + 7:lines.find("|") + 12]
                        Temp_list.append(int(Temp) / 1000)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    CPU_TEMP_item_type = "time"
                    if CPU_TEMP_current_type == None or CPU_TEMP_current_type != "time":
                        CPU_TEMP_current_type = CPU_TEMP_item_type
                        System_time = lines[:19]
                        CPU_TEMP_Date.append(System_time)

                if "com.moredian.entrance.guard (pid" in str(lines) and "moredianMem" in str(lines):  # Argus_PID
                    Argus_PID_item_type = "data"
                    if Argus_PID_current_type == "time":
                        Argus_PID_current_type = Argus_PID_item_type
                        Argus_pid = lines[lines.find("pid") + 4:lines.find("/") - 1]
                        Pid_list.append(Argus_pid)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    Argus_PID_item_type = "time"
                    if Argus_PID_current_type == None or Argus_PID_current_type != "time":
                        Argus_PID_current_type = Argus_PID_item_type
                        System_time = lines[:19]
                        Argus_PID_Date.append(System_time)

            except ValueError:
                lable_D2P = Text(root,height=4)
                lable_D2P.insert("1.0","源数据格式错误"+'\n'+path + "\\" + file+'\n'+lines)
                lable_D2P.place(x=100,y=120)
                return

    PLT_CPU(CPU_Date,CPU_radio_list)
    PLT_MEM(Free_Date, Free_RAM_list)
    PLT_APK_CPU(APK_CPU_Date, apk_cpu_radio_list)
    PLT_APK_MEM(APK_MEM_Date, apk_RAM_list)
    PLT_CPU_TEMP(CPU_TEMP_Date, Temp_list)
    PLT_Argus_PID(Argus_PID_Date, Pid_list)

def D3(path,files,CPU_Date,Free_Date,APK_CPU_Date,APK_MEM_Date,CPU_TEMP_Date,Argus_PID_Date,CPU_radio_list,Free_RAM_list,apk_cpu_radio_list,apk_RAM_list,Temp_list,Pid_list):
    CPU_current_type = MEM_current_type = APK_CPU_current_type = APK_MEM_current_type = CPU_TEMP_current_type = Argus_PID_current_type = None

    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            try:
                if "800%" in str(lines):  # CPU_ALL
                    CPU_item_type = "data"
                    if CPU_current_type == "time":
                        CPU_current_type = CPU_item_type
                        CPU_radio = (800 - int(lines[lines.find("sys") + 4:lines.find("idle") - 1]))  # CPU_ALL
                        CPU_radio_list.append(float(CPU_radio) / 8)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    CPU_item_type = "time"
                    if CPU_current_type == None or CPU_current_type != "time":
                        CPU_current_type = CPU_item_type
                        System_time = lines[:19]
                        CPU_Date.append(System_time)

                if "Free RAM" in str(lines):                                                                                # MEM_ALL
                    MEM_item_type = "data"
                    if MEM_current_type == "time":
                        MEM_current_type = MEM_item_type
                        Free_RAM = int(str(lines[lines.find("RAM:") + 6:lines.find(",")]) + str(
                            lines[lines.find(",") + 1:lines.find("K")]))
                        Free_RAM_list.append(int(Free_RAM))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    MEM_item_type = "time"
                    if MEM_current_type == None or MEM_current_type != "time":
                        MEM_current_type = MEM_item_type
                        System_time = lines[:19]
                        Free_Date.append(System_time)

                if "u0_a" in str(lines) and "com.moredian.entrance.guard" in str(lines) and "channel" not in lines:  # APK_CPU
                    APK_CPU_item_type = "data"
                    if APK_CPU_current_type == "time":
                        APK_CPU_current_type = APK_CPU_item_type
                        apk_cpu_radio = float(lines[lines.find("M") + 10:lines.find("com.moredian.entrance.guard") - 17])
                        apk_cpu_radio_list.append(int(apk_cpu_radio) / 8)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    APK_CPU_item_type = "time"
                    if APK_CPU_current_type == None or APK_CPU_current_type != "time":
                        APK_CPU_current_type = APK_CPU_item_type
                        System_time = lines[:19]
                        APK_CPU_Date.append(System_time)

                if "moredianMem" in str(lines):                                                                             #APK_MEM
                    APK_MEM_item_type = "data"
                    if APK_MEM_current_type == "time":
                        APK_MEM_current_type = APK_MEM_item_type
                        apk_RAM = int(str(int((lines[lines.find(":") + 1:lines.find(",")]) + str(
                            lines[lines.find(",") + 1:lines.find("K")]))))  # D2P
                        apk_RAM_list.append(int(apk_RAM))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    APK_MEM_item_type = "time"
                    if APK_MEM_current_type == None or APK_MEM_current_type != "time":
                        APK_MEM_current_type = APK_MEM_item_type
                        System_time = lines[:19]
                        APK_MEM_Date.append(System_time)

                if "getTempResult" in str(lines):                                                                           # CPU_TEMP
                    CPU_TEMP_item_type = "data"
                    if CPU_TEMP_current_type == "time":
                        CPU_TEMP_current_type = CPU_TEMP_item_type
                        Temp = lines[lines.find("|") + 9:lines.find("|") + 14]
                        Temp_list.append(int(Temp) / 1000)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    CPU_TEMP_item_type = "time"
                    if CPU_TEMP_current_type == None or CPU_TEMP_current_type != "time":
                        CPU_TEMP_current_type = CPU_TEMP_item_type
                        System_time = lines[:19]
                        CPU_TEMP_Date.append(System_time)

                if "com.moredian.entrance.guard (pid" in str(lines) and "moredianMem" in str(lines):                        # Argus_PID
                    Argus_PID_item_type = "data"
                    if Argus_PID_current_type == "time":
                        Argus_PID_current_type = Argus_PID_item_type
                        Argus_pid = lines[lines.find("pid") + 4:lines.find("/") - 1]
                        Pid_list.append(Argus_pid)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    Argus_PID_item_type = "time"
                    if Argus_PID_current_type == None or Argus_PID_current_type != "time":
                        Argus_PID_current_type = Argus_PID_item_type
                        System_time = lines[:19]
                        Argus_PID_Date.append(System_time)
            except ValueError:
                lable_D3 = Text(root, height=4)
                lable_D3.insert("1.0", "源数据格式错误" + '\n' + path + "\\" + file + '\n' + lines)
                lable_D3.place(x=100, y=120)
                return

    PLT_CPU(CPU_Date,CPU_radio_list)
    PLT_MEM(Free_Date, Free_RAM_list)
    PLT_APK_CPU(APK_CPU_Date, apk_cpu_radio_list)
    PLT_APK_MEM(APK_MEM_Date, apk_RAM_list)
    PLT_CPU_TEMP(CPU_TEMP_Date, Temp_list)
    PLT_Argus_PID(Argus_PID_Date, Pid_list)

def D2_D2A(path,files,CPU_Date,Free_Date,APK_CPU_Date,APK_MEM_Date,CPU_TEMP_Date,Argus_PID_Date,CPU_radio_list,Free_RAM_list,apk_cpu_radio_list,apk_RAM_list,Temp_list,Pid_list):
    CPU_current_type = MEM_current_type = APK_CPU_current_type = APK_MEM_current_type = CPU_TEMP_current_type = Argus_PID_current_type = None

    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            try:
                if "---cpu:U" in str(lines):  # CPU_ALL
                    CPU_item_type = "data"
                    if CPU_current_type == "time":
                        CPU_current_type = CPU_item_type
                        CPU_radio = (int(lines[lines.find("User") + 5:lines.find("System") - 3]) + int(
                            lines[lines.find("System") + 7:lines.find("IOW") - 3]) + int(
                            lines[lines.find("IOW") + 4:lines.find("IRQ") - 3]))  # D2P
                        CPU_radio_list.append(float(CPU_radio))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    CPU_item_type = "time"
                    if CPU_current_type == None or CPU_current_type != "time":
                        CPU_current_type = CPU_item_type
                        System_time = lines[:19]
                        CPU_Date.append(System_time)

                if "Free RAM" in str(lines):                                                                            # MEM_ALL
                    MEM_item_type = "data"
                    if MEM_current_type == "time":
                        MEM_current_type = MEM_item_type
                        Free_RAM = int(str(lines[lines.find("RAM:") + 5:lines.find("k") - 1]))
                        Free_RAM_list.append(int(Free_RAM))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    MEM_item_type = "time"
                    if MEM_current_type == None or MEM_current_type != "time":
                        MEM_current_type = MEM_item_type
                        System_time = lines[:19]
                        Free_Date.append(System_time)

                if "u0_a19" in str(lines) and "com.moredian.entrance.guard" in str(lines) and "channel" not in lines:  # APK_CPU
                    APK_CPU_item_type = "data"
                    if APK_CPU_current_type == "time":
                        APK_CPU_current_type = APK_CPU_item_type
                        apk_cpu_radio = float(lines[lines.find("%") - 2:lines.find("%")])
                        apk_cpu_radio_list.append(int(apk_cpu_radio))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    APK_CPU_item_type = "time"
                    if APK_CPU_current_type == None or APK_CPU_current_type != "time":
                        APK_CPU_current_type = APK_CPU_item_type
                        System_time = lines[:19]
                        APK_CPU_Date.append(System_time)

                if "moredianMem" in str(lines):                                                                             #APK_MEM
                    APK_MEM_item_type = "data"
                    if APK_MEM_current_type == "time":
                        APK_MEM_current_type = APK_MEM_item_type
                        apk_RAM = int(str(int((lines[lines.find(":") + 1:lines.find("k") - 1]))))  # D2P
                        apk_RAM_list.append(int(apk_RAM))
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    APK_MEM_item_type = "time"
                    if APK_MEM_current_type == None or APK_MEM_current_type != "time":
                        APK_MEM_current_type = APK_MEM_item_type
                        System_time = lines[:19]
                        APK_MEM_Date.append(System_time)

                if "getTempResult" in str(lines):                                                                           # CPU_TEMP
                    CPU_TEMP_item_type = "data"
                    if CPU_TEMP_current_type == "time":
                        CPU_TEMP_current_type = CPU_TEMP_item_type
                        Temp = lines[lines.find("|") + 9:lines.find("|") + 14]
                        Temp_list.append(int(Temp) / 1000)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    CPU_TEMP_item_type = "time"
                    if CPU_TEMP_current_type == None or CPU_TEMP_current_type != "time":
                        CPU_TEMP_current_type = CPU_TEMP_item_type
                        System_time = lines[:19]
                        CPU_TEMP_Date.append(System_time)

                if "com.moredian.entrance.guard (pid" in str(lines) and "moredianMem" in str(lines):                        # Argus_PID
                    Argus_PID_item_type = "data"
                    if Argus_PID_current_type == "time":
                        Argus_PID_current_type = Argus_PID_item_type
                        Argus_pid = lines[lines.find("pid") + 4:lines.find("/") - 1]
                        Pid_list.append(Argus_pid)
                if "DumpDevStateService" in str(lines) and "before" in str(lines):
                    Argus_PID_item_type = "time"
                    if Argus_PID_current_type == None or Argus_PID_current_type != "time":
                        Argus_PID_current_type = Argus_PID_item_type
                        System_time = lines[:19]
                        Argus_PID_Date.append(System_time)
            except ValueError:
                lable_D2_D2A = Text(root, height=4)
                lable_D2_D2A.insert("1.0", "源数据格式错误" + '\n' + path + "\\" + file + '\n' + lines)
                lable_D2_D2A.place(x=100, y=120)
                return


    PLT_CPU(CPU_Date,CPU_radio_list)
    PLT_MEM(Free_Date, Free_RAM_list)
    PLT_APK_CPU(APK_CPU_Date, apk_cpu_radio_list)
    PLT_APK_MEM(APK_MEM_Date, apk_RAM_list)
    PLT_CPU_TEMP(CPU_TEMP_Date, Temp_list)
    PLT_Argus_PID(Argus_PID_Date, Pid_list)

def find_data():
    path = Entry_FilePath.get("1.0","end-1c")
    files = os.listdir(path)
    if Var.get() == 1:
        D2P(path,files,CPU_Date=[],Free_Date=[],APK_CPU_Date=[],APK_MEM_Date=[],CPU_TEMP_Date=[],Argus_PID_Date=[],CPU_radio_list=[],Free_RAM_list=[],apk_cpu_radio_list=[],apk_RAM_list=[],Temp_list=[],Pid_list=[])
    elif Var.get() == 2:
        D3(path, files, CPU_Date=[], Free_Date=[], APK_CPU_Date=[], APK_MEM_Date=[], CPU_TEMP_Date=[],
           Argus_PID_Date=[], CPU_radio_list=[], Free_RAM_list=[], apk_cpu_radio_list=[], apk_RAM_list=[], Temp_list=[],
           Pid_list=[])
    elif Var.get() == 3:
        D2_D2A(path, files, CPU_Date=[], Free_Date=[], APK_CPU_Date=[], APK_MEM_Date=[], CPU_TEMP_Date=[],
               Argus_PID_Date=[], CPU_radio_list=[], Free_RAM_list=[], apk_cpu_radio_list=[], apk_RAM_list=[],
               Temp_list=[], Pid_list=[])

root = Tk()
root.title("SelectData")
root.geometry('800x200+500+300') # 全局界面大小
# root.wm_attributes('-topmost', 1) # 永远保持最前
Var = IntVar()
Var.set(1)

Data_FilePath = tkinter.Label(root,text="文件路径：",borderwidth=1,width=10).place(x=20,y=80)
Entry_FilePath = Text(root,height=2)
Entry_FilePath.insert("1.0",r"E:\Moredian\tools\stability\20240419_102922\com.moredian.mdservice\DumpDevStateService")
Entry_FilePath.place(x=100,y=80)
product_D2P = Radiobutton(root,text="D2PLUS",variable=Var,value=1).place(x=20,y=10)
product_D3 = Radiobutton(root,text="D3",variable=Var,value=2).place(x=20,y=30)
product_D2_D2A = Radiobutton(root,text="D2_D2A",variable=Var,value=3).place(x=20,y=50)

comand = Button(root, text="获取", command=find_data,width=8, height=2,borderwidth=2).place(x=20,y=120)

root.mainloop()