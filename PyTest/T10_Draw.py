import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def CPU(path,files,Date,Data,C):
    for file in files:
        with open(path + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:16])
            C.append(D)
            for i in data.split("\n"):
                if "TOTAL" in i :
                    Data.append(round(int(str(i)[:i.find("%")]),2))
                    Date.append(D)
    # print(Data)
    tick_spacing = 15
    fig,ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Data)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_ALL",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("%",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def Free_MEM(path1,files1,Date,Data,C):
    for file in files1:
        with open(path1 + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:16])
            C.append(D)
            for i in data.split("\n"):
                if "TOTAL SWAP PSS" in i :
                    Data.append(int(str(i)[i.find("TOTAL")+9:i.find("TOTAL")+16]))
                    Date.append(D)

    tick_spacing = 15
    fig,ax_Free = plt.subplots(1, 1)
    ax_Free.plot(Date, Data)
    ax_Free.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Free_MEM_ALL",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("KB",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def APK_CPU(path2,Date,Data,C):
    # for file in files2:
    with open(path2 + "\\" + "apkcpu.log",encoding="utf-8") as f:
        data = f.read()

        for i in data.split("\n"):
            if "u0_a" in i and "S" in i and "2024" in i:
                Data.append((float(str(i)[i.find("S")+2:i.find("S")+6])/6))
                D = (i[5:16])
                C.append(D)
                Date.append(D)
            if "u0_a" in i and "R" in i and "2024" in i:
                Data.append((float(str(i)[i.find("R")+2:i.find("R")+6])/6))
                D = (i[5:16])
                C.append(D)
                Date.append(D)
    tick_spacing = 800
    fig,ax_APK_MEM = plt.subplots(1, 1)
    ax_APK_MEM.plot(Date, Data)
    ax_APK_MEM.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_CPU",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("%",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def APK_MEM(path2,Date,Data,C):
    with open(path2 + "\\" + "apkMem.log",encoding="utf-8") as f:
        data = f.read()
        for i in data.split("\n"):
            if "com.moredian.entrance.guard" in i:
                Data.append(int((str(i[i.find("#") + 2 :i.find("#")+5]))+str(i[i.find(",") +1 :i.find(",")+4])))
                D = str(i)[5:16]
                C.append(D)
                Date.append(D)
    tick_spacing = 800
    fig,ax_APK_CPU = plt.subplots(1, 1)
    ax_APK_CPU.plot(Date, Data)
    ax_APK_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_MEM",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("KB",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def CPU_TEMP(path,Date,Data,C):
    with open(path + "\\" + "cpu_temp.log",encoding="utf-8") as f:
        data = f.read()
        for i in data.split("\n"):
            if "#" in i:
                Data.append(round(float(str(i)[-5:])/1000,2))
                D = (str(i)[5:13])
                C.append(D)
                Date.append(D)
    # print(Data)
    tick_spacing = 10
    fig,ax_CPU_TEMP = plt.subplots(1, 1)
    ax_CPU_TEMP.plot(Date, Data)
    ax_CPU_TEMP.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_TEMP",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("℃",fontsize=12,rotation=0,labelpad=10)
    plt.show()

path = r"C:\Users\Administrator\Desktop\0050\0050\dumpsys_cpuinfo"
path1 = r"C:\Users\Administrator\Desktop\0050\0050\dumpsys_meminfo"
path2 = r"C:\Users\Administrator\Desktop\0050\0050\others"
files = os.listdir(path)
files1 = os.listdir(path1)
files2 = os.listdir(path2)


CPU(path,files,Date=[],Data=[],C=[])
Free_MEM(path1,files1,Date=[],Data=[],C=[])
APK_CPU(path2,Date=[],Data=[],C=[])
APK_MEM(path2,Date=[],Data=[],C=[])
CPU_TEMP(path2,Date=[],Data=[],C=[])


