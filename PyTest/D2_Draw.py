import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def CPU(path,files,Date,CPU_radio_list):
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "---cpu:U" in str(lines):
                CPU_radio = (int(lines[lines.find("User") + 5:lines.find("System") - 3]) + int(
                    lines[lines.find("System") + 7:lines.find("IOW") - 3]) + int(
                    lines[lines.find("IOW") + 4:lines.find("IRQ") - 3]))  # D2P
                CPU_radio_list.append(float(CPU_radio))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    # print(Data)
    # if len(CPU_radio_list) != len(Date):
    #     CPU_radio_list = Date = CPU_radio_list[0,min(len(CPU_radio_list),len(Date))]
    tick_spacing = 500
    fig,ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, CPU_radio_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_ALL",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("%",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def Free_MEM(path,files,Date,Free_RAM_list):
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "Free RAM" in str(lines):
                Free_RAM = int(str(lines[lines.find("RAM:") + 5:lines.find("k") - 1]))
                Free_RAM_list.append(int(Free_RAM))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    # print(Data)
    tick_spacing = 800
    fig,ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Free_RAM_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Free_RAM",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("KB",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def APK_CPU(path,files,Date,apk_cpu_radio_list):
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "u0_a19" in str(lines) and "com.moredian.entrance.guard" in str(lines) and "channel" not in lines:  # D2PLUS
                apk_cpu_radio = float(lines[lines.find("%") - 2:lines.find("%")])
                apk_cpu_radio_list.append(int(apk_cpu_radio))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    tick_spacing = 800
    fig,ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, apk_cpu_radio_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_CPU",loc="center")
    plt.xlabel('Time',fontsize=12)
    plt.ylabel("%",fontsize=12,rotation=0,labelpad=10)
    plt.show()


def APK_MEM(path,files,Date,apk_RAM_list):
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "moredianMem" in str(lines):
                apk_RAM = int(str(int((lines[lines.find(":") + 1:lines.find("k") - 1]))))  # D2P
                apk_RAM_list.append(int(apk_RAM))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    tick_spacing = 800
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, apk_RAM_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_MEM", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("KB", fontsize=12, rotation=0, labelpad=10)
    plt.show()


def CPU_TEMP(path,files,Date,Temp_list):
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "getTempResult" in str(lines):
                Temp = lines[lines.find("|") + 9:lines.find("|") + 14]
                Temp_list.append(int(Temp) / 1000)
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    tick_spacing = 800
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Temp_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_TEMP", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("℃", fontsize=12, rotation=0, labelpad=10)
    plt.show()

def Argus_PID(path,files,Date,Pid_list):
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "com.moredian.entrance.guard (pid" in str(lines) and "moredianMem" in str(lines):
                Argus_pid = lines[lines.find("pid") + 4:lines.find("/") - 1]
                Pid_list.append(Argus_pid)

            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    tick_spacing = 800
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Pid_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Argus_PID", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("pid", fontsize=12, rotation=0, labelpad=10)
    plt.show()

path = r"E:\Moredian\tools\stability\20240411_160203\com.moredian.mdservice\DumpDevStateService"
files = os.listdir(path)


CPU(path,files,Date=[],CPU_radio_list=[])
Free_MEM(path,files,Date=[],Free_RAM_list=[])
APK_CPU(path,files,Date=[],apk_cpu_radio_list=[])
APK_MEM(path,files,Date=[],apk_RAM_list=[])
CPU_TEMP(path,files,Date=[],Temp_list=[])
Argus_PID(path,files,Date=[],Pid_list=[])


