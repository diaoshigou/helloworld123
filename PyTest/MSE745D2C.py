import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def CPU(path,files,Date,CPU_radio_list):
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "600%cpu" in str(lines):
                CPU_radio = (600-int(lines[lines.find("idle") - 4:lines.find("idle") - 1]))  # MSE745D2C

                CPU_radio_list.append(float(CPU_radio)/6)
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    # print(Data)
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
                Free_RAM = int(str(lines[lines.find("RAM:") + 7:lines.find("RAM:") + 10]) + str(lines[lines.find("K") - 3:lines.find("K")]))
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
            if "u0_a" in str(lines) and "com.moredian.entrance.guard" in str(lines) and "S" in lines and "channel" not in lines:  # D2PLUS
                apk_cpu_radio = float(lines[lines.find("S") + 2:lines.find("S") + 6])
                # print(apk_cpu_radio)
                apk_cpu_radio_list.append(int(apk_cpu_radio)/6)
            if "u0_a" in str(lines) and "com.moredian.entrance.guard" in str(lines) and "R" in lines and "channel" not in lines:  # D2PLUS
                apk_cpu_radio = float(lines[lines.find("R") + 2:lines.find("R") + 6])
                # print(apk_cpu_radio)
                apk_cpu_radio_list.append(int(apk_cpu_radio)/6)
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                # print(System_time)
                Date.append(System_time)
    tick_spacing = 800
    if len(apk_cpu_radio_list) > len(Date):
        apk_cpu_radio_list = len(Date)
    else:
        Date = Date[:len(apk_cpu_radio_list)]
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
            if "moredianMem" in str(lines) and "K" in str(lines):
                apk_RAM = int(str(lines[lines.find(":") + 1:lines.find(",")]) + str(lines[lines.find(",") + 1:lines.find(",") + 4]))  # MSE745D2C
                # print(apk_RAM)
                apk_RAM_list.append(int(apk_RAM))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                System_time = lines[:19]
                Date.append(System_time)
    tick_spacing = 800
    if len(apk_RAM_list) > len(Date):
        apk_cpu_radio_list = len(Date)
    else:
        Date = Date[:len(apk_RAM_list)]
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
                Temp = lines[lines.find("|") + 7:lines.find("|") + 12]
                # Write(Temp_list_row, int(Temp) / 1000)
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
    if len(Pid_list) > len(Date):
        apk_cpu_radio_list = len(Date)
    else:
        Date = Date[:len(Pid_list)]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Pid_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Argus_PID", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("pid", fontsize=12, rotation=0, labelpad=10)
    plt.show()

path = r"E:\Moredian\tools\stability\20240129_100326\com.moredian.mdservice\DumpDevStateService"
files = os.listdir(path)


CPU(path,files,Date=[],CPU_radio_list=[])
Free_MEM(path,files,Date=[],Free_RAM_list=[])
APK_CPU(path,files,Date=[],apk_cpu_radio_list=[])
APK_MEM(path,files,Date=[],apk_RAM_list=[])
CPU_TEMP(path,files,Date=[],Temp_list=[])
Argus_PID(path,files,Date=[],Pid_list=[])


