import os

def CPU_D2P():
    io_array = []
    try:
        for i in range(3):
            # f2 = open(os.getcwd()+'\CPU_D2P.txt', 'a')
            output = os.popen('adb shell top -n 1|findstr "cpu"')
            io = output.read()
            # f2.write(io)
            io_array.append((600 - int(io[io.find('sys') + 4:io.find("idle") - 1])) / 6)
            # f2.close()
        print(" CPU总占用率：" + str(round(sum(io_array) / len(io_array), 2)) + "%(" + str(
            round(max(io_array), 2)) + "%-" + str(round(min(io_array), 2)) + "%" + ')')
    except Exception as e:
        print(e)

def APK_cpu_D2P():
    io_array = []
    try:
        for i in range(3):
            # f2 = open('D:\log\D2-D-cpu_static.txt', 'a')
            output = os.popen('adb shell top -n 1|findstr "com.moredian" ')
            # print("第"+str(i)+"次")
            io = output.read()
            # print(type(float(io[43:47])))
            # print(float(io[43:47]))
            io_array.append(float(io[43:47]))
            # f2.close()
        print(" APK占用CPU：" + str(round(sum(io_array) / len(io_array), 2)) + "%(" + str(
            round(max(io_array), 2)) + "%-" + str(round(min(io_array), 2)) + "%)")
    except Exception as e:
        print(e)

def Sysmem_D2P():
    io_array = []
    try:
        for i in range(3):
            # f2 = open('D:\log\D2-D-cpu_static.txt', 'a')
            output = os.popen('adb shell dumpsys meminfo | findstr "Free" ')
            # print("第"+str(i)+"次")
            io = output.read()
            # print(type(io[13:16]+io[17:20]))
            # print(io[13:16]+io[17:20])
            io_array.append(float(io[13:16]+io[17:20]))
        #     # f2.close()
        print(" APK占用CPU：" + str(round(sum(io_array) / len(io_array), 2)) + "KB(" + str(
            round(max(io_array), 2)) + "KB-" + str(round(min(io_array), 2)) + "KB)")
    except Exception as e:
        print(e)

def APKmem_D2P():
    io_array = []
    try:
        for i in range(2):
            # f2 = open('D:\log\D2-D-cpu_static.txt', 'a')
            output = os.popen('adb shell dumpsys meminfo | findstr "com.moredian.entrance.guard" ')
            # print("第"+str(i)+"次")
            io = output.read()
            # print(type(float(io[43:47])))
            # print(int(io[4:7] + io[8:11]))
            io_array.append(float(io[4:7] + io[8:11]))
            #     # f2.close()
        print(" APK占用CPU：" + str(round(sum(io_array) / len(io_array), 2)) + "KB(" + str(
            round(max(io_array), 2)) + "KB-" + str(round(min(io_array), 2)) + "KB)")
    except Exception as e:
        print(e)

def Temp_D2P():
    io_array = []
    try:
        for i in range(3):
            # f2 = open('D:\log\D2-D-cpu_static.txt', 'a')
            output = os.popen('adb shell cat /sys/class/thermal/thermal_zone1/temp ')
            io = output.read()
            # print(int(io)/1000)
            io_array.append(float(io)/1000)
            #     # f2.close()
        print(" APK占用CPU：" + str(round(sum(io_array) / len(io_array), 2)) + "℃(" + str(
            round(max(io_array), 2)) + "℃-" + str(round(min(io_array), 2)) + "℃)")
    except Exception as e:
        print(e)

# CPU_D2P()
# APK_cpu_D2P()
# Sysmem_D2P()
# APKmem_D2P()
Temp_D2P()