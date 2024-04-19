import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# fig = plt.figure(figsize=(12,4),dpi=300)
def Free_MEM(path,files,Date,Data,C):
    for file in files:
        # print(file)
        with open(path + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:13])
            C.append(D)
            for i in data.split("\n"):
                if "Free RAM" in i :
                    Data.append(int(str(i)[i.find("RAM")+7:i.find("K")-4]+str(i)[i.find("K")-3:i.find("K")]))
                    Date.append(D)
    tick_spacing = 10
    fig,ax_Free = plt.subplots(1, 1)
    ax_Free.plot(Date, Data)
    ax_Free.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Free_MEM_ALL",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("KB",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def APK_MEM(path,files,Date,Data,C):
    for file in files:
        with open(path + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:13])
            C.append(D)
            for i in data.split("\n"):
                if "---moredianMem" in i and "com.moredian.entrance.guard" in i :
                    Data.append(int(str(i)[i.find("moredianMem")+12:i.find("K")-4]+str(i)[i.find("K")-3:i.find("K")]))
                    Date.append(D)
    tick_spacing = 10
    fig,ax_APK_MEM = plt.subplots(1, 1)
    ax_APK_MEM.plot(Date, Data)
    ax_APK_MEM.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_MEM",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("KB",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def CPU(path,files,Date,Data,C):
    for file in files:
        # print(file)
        with open(path + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:13])
            C.append(D)
            for i in data.split("\n"):
                if "%cpu" in i :
                    # print(i)
                    Data.append(round((600-int(str(i)[i.find("sys")+4:i.find("idle")-1]))/6,2))
                    Date.append(D)
    # print(Data)
    tick_spacing = 10
    fig,ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Data)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_ALL",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("%",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def APK_CPU(path,files,Date,Data,C):
    for file in files:
        # print(file)
        with open(path + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:13])
            C.append(D)
            for i in data.split("\n"):
                if "com.moredian.entrance.guard" in i and "u0_a17" in i and "channel" not in i:
                    # print(i)
                    Data.append(round(float(i[i.find("com.moredian.entrance.guard") - 21 :i.find("com.moredian.entrance.guard")-17])/6,2))
                    Date.append(D)
    # print(Data)
    tick_spacing = 10
    fig,ax_APK_CPU = plt.subplots(1, 1)
    ax_APK_CPU.plot(Date, Data)
    ax_APK_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_CPU",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("%",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def CPU_TEMP(path,files,Date,Data,C):
    for file in files:
        with open(path + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:13])
            C.append(D)
            for i in data.split("\n"):
                if "---cpuTemp" in i:
                    Data.append(round(float(str(i)[i.find("cpuTemp")+8:i.find("pmic")-1])/1000,2))
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


def PMIC_TEMP(path,files,Date,Data,C):
    for file in files:
        with open(path + "\\" + file,encoding="utf-8") as f:
            data = f.read()
            D = (str(data)[5:13])
            C.append(D)
            for i in data.split("\n"):
                if "pmicTemp" in i:
                    Data.append(round(float(str(i)[i.find("pmicTemp")+9:])/1000,2))
                    Date.append(D)
    tick_spacing = 10
    fig,ax_PMIC_TEMP = plt.subplots(1, 1)
    ax_PMIC_TEMP.plot(Date, Data)
    ax_PMIC_TEMP.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("PMIC_TEMP",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("℃",fontsize=12,rotation=0,labelpad=10)
    plt.show()

path = r"E:\Moredian\tools\stability\logs\DumpDevStateService"
files = os.listdir(path)

Free_MEM(path,files,Date=[],Data=[],C=[])
APK_MEM(path,files,Date=[],Data=[],C=[])
CPU(path,files,Date=[],Data=[],C=[])
APK_CPU(path,files,Date=[],Data=[],C=[])
CPU_TEMP(path,files,Date=[],Data=[],C=[])
PMIC_TEMP(path,files,Date=[],Data=[],C=[])


