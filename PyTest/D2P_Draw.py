import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


current_type = None
item_type = None

def PLT_CPU(Date,CPU_radio_list):
    tick_spacing = (len(Date) / 8)
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, CPU_radio_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_ALL", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("%", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45, fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

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


def D2P(path,files,CPU_Date,CPU_radio_list):
    global current_type,item_type
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "600%cpu" in str(lines):     # CPU_D2P
                item_type = "data"
                if current_type == "time":
                    current_type = item_type
                    CPU_radio = (int(lines[lines.find("sys") + 4:lines.find("idle") - 1]))  # D2P
                    CPU_radio_list.append(float(CPU_radio)/6)
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                item_type = "time"
                if current_type == None or current_type != "time":
                    current_type = item_type
                    System_time = lines[:19]
                    CPU_Date.append(System_time)
    PLT_CPU(CPU_Date,CPU_radio_list)

def Free_MEM_D2P(path,files,Free_Date,Free_RAM_list):
    global current_type, item_type
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "Free RAM" in str(lines):
                item_type = "data"
                if current_type == "time":
                    current_type = item_type
                    Free_RAM = int(str(lines[lines.find("RAM:") + 7:lines.find(",")])+str(lines[lines.find(",") + 1:lines.find("K")]))
                    Free_RAM_list.append(int(Free_RAM))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                item_type = "time"
                if current_type == None or current_type != "time":
                    current_type = item_type
                    System_time = lines[:19]
                    Free_Date.append(System_time)
    PLT_MEM(Free_Date,Free_RAM_list)

def APK_CPU_D2P(path,files,Date,apk_cpu_radio_list):
    global current_type, item_type
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "u0_a" in str(lines) and "com.moredian.entrance.guard" in str(lines) and "S" in lines and "channel" not in lines:  # D2PLUS
                item_type = "data"
                if current_type == "time":
                    current_type = item_type
                    apk_cpu_radio = float(lines[lines.find("S") + 2:lines.find("S") + 6])
                    apk_cpu_radio_list.append(int(apk_cpu_radio))
            if "u0_a" in str(lines) and "com.moredian.entrance.guard" in str(lines) and "R" in lines and "channel" not in lines:  # D2PLUS
                item_type = "data"
                if current_type == "time":
                    current_type = item_type
                    apk_cpu_radio = float(lines[lines.find("R") + 2:lines.find("R") + 6])
                    apk_cpu_radio_list.append(int(apk_cpu_radio))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                item_type = "time"
                if current_type == None or current_type != "time":
                    current_type = item_type
                    System_time = lines[:19]
                    Date.append(System_time)
    PLT_APK_CPU(Date, apk_cpu_radio_list)

def APK_MEM_D2P(path,files,Date,apk_RAM_list):
    global current_type, item_type
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "moredianMem" in str(lines):
                item_type = "data"
                if current_type == "time":
                    current_type = item_type
                    apk_RAM = int(str(lines[lines.find(":") + 1:lines.find(",")])+str(lines[lines.find(",") + 1:lines.find("K")]))  # D2P
                    apk_RAM_list.append(int(apk_RAM))
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                item_type = "time"
                if current_type == None or current_type != "time":
                    current_type = item_type
                    System_time = lines[:19]
                    Date.append(System_time)
    tick_spacing = (len(Date)/8)
    if len(apk_RAM_list) != len(Date):
        apk_RAM_list = apk_RAM_list[:int(min(len(apk_RAM_list),len(Date)))]
        Date = Date[:int(min(len(apk_RAM_list),len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, apk_RAM_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("APK_MEM", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("KB", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45,fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

def CPU_TEMP_D2P(path,files,Date,Temp_list):
    global current_type, item_type
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "getTempResult" in str(lines):
                item_type = "data"
                if current_type == "time":
                    current_type = item_type
                    Temp = lines[lines.find("|") + 7:lines.find("|") + 12]
                    Temp_list.append(int(Temp) / 1000)
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                item_type = "time"
                if current_type == None or current_type != "time":
                    current_type = item_type
                    System_time = lines[:19]
                    Date.append(System_time)
    tick_spacing = (len(Date)/8)
    if len(Temp_list) != len(Date):
        Temp_list = Temp_list[:int(min(len(Temp_list),len(Date)))]
        Date = Date[:int(min(len(Temp_list),len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Temp_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("CPU_TEMP", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("℃", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45,fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

def Argus_PID_D2P(path,files,Date,Pid_list):
    global current_type, item_type
    for file in files:
        fopen = open(path + "\\" + file, encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "com.moredian.entrance.guard (pid" in str(lines) and "moredianMem" in str(lines):
                item_type = "data"
                if current_type == "time":
                    current_type = item_type
                    Argus_pid = lines[lines.find("pid") + 4:lines.find("/") - 1]
                    Pid_list.append(Argus_pid)
            if "DumpDevStateService" in str(lines) and "after" in str(lines):
                item_type = "time"
                if current_type == None or current_type != "time":
                    current_type = item_type
                    System_time = lines[:19]
                    Date.append(System_time)
    tick_spacing = (len(Date)/8)
    if len(Pid_list) != len(Date):
        Pid_list = Pid_list[:int(min(len(Pid_list),len(Date)))]
        Date = Date[:int(min(len(Pid_list),len(Date)))]
    fig, ax_CPU = plt.subplots(1, 1)
    ax_CPU.plot(Date, Pid_list)
    ax_CPU.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.title("Argus_PID", loc="center")
    plt.xlabel('Time', fontsize=12)
    plt.ylabel("pid", fontsize=12, rotation=0, labelpad=10)
    plt.xticks(rotation=45,fontsize=8)
    plt.subplots_adjust(bottom=0.26)
    plt.show()

path = r"E:\Moredian\tools\stability\20240419_102922\com.moredian.mdservice\DumpDevStateService"
files = os.listdir(path)


D2P(path,files,CPU_Date=[],CPU_radio_list=[])
# Free_MEM_D2P(path,files,Date=[],Free_RAM_list=[])
# APK_CPU_D2P(path,files,Date=[],apk_cpu_radio_list=[])
# APK_MEM_D2P(path,files,Date=[],apk_RAM_list=[])
# CPU_TEMP_D2P(path,files,Date=[],Temp_list=[])
# Argus_PID_D2P(path,files,Date=[],Pid_list=[])


