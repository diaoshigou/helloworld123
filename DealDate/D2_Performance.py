import os
import subprocess
from datetime import datetime
from time import sleep

def CPU_D2():
    sum_out = []
    for number in range(1, 3):
        try:
            output = os.popen("adb shell top -n 1 | findstr System ").read()
            User = int(output[output.find('User') + 5:output.find('System') - 3])
            System = int(output[output.find('System') + 7:output.find('IOW') - 3])
            IOW = int(output[output.find('IOW') + 4:output.find('IRQ') - 3])
            IRQ = int(output[output.find('IRQ') + 4:output.rindex('%')])
            with open(path+"\CPU_D2.txt", 'a+') as f:  # 设置文件对象
                f.write("User:" + str(User) + '%,' + "System:" + str(System) + '%,' + "IOW:" + str(
                    IOW) + '%,' + "IRQ:" + str(IRQ) + '%\n')
                f.write("时间:" + str(datetime.now()) + '\n')
                sum_out.append(User + System + IOW + IRQ)
                sum = 0
                for i in sum_out:
                    sum = sum + i
                ave = sum / len(sum_out)
                sleep(5)
                # print("已完成")
                f.write("ave:" + str(ave) + '%\n')
                f.close()
                APK_cpu_D2()
        except Exception as e:
            print(e)

def APK_cpu_D2():
    sum_out = []
    # sum_out.clear()
    for number in range(1 , 2):
        try:
            output = os.popen("adb shell top -n 1 | findstr com.moredian.entrance.guard ").read()
            with open(path + r'\APK_cpu_D2.txt', 'a+') as f:  # 设置文件对象
                # print(output[:79])
                f.write(output[:79] + '\n')
                sum_out.append(int(output[10:12]))
                sum = 0
                for i in sum_out:
                    sum = sum + i
                ave = sum / len(sum_out)
                f.write("ave:" + str(ave) + '%\n')
                f.write("时间:" + str(datetime.now()) + '\n')
                # sleep(5)
                # print("已完成")
                # Sysmem_D2()
        except Exception as e:
            print(e)

def Sysmem_D2():
    sum_out = []
    for number in range(1, 2):
        try:
            output = os.popen("adb shell dumpsys meminfo|findstr Free ").read()
            RAM = int(output[11:output.find('kB') - 1])
            with open( path + r'\meminfo-Free.txt', 'a+') as f:  # 设置文件对象
                f.write("Free RAM:" + str(RAM) + 'KB' + '\n')
                sum_out.append(RAM)
                sum = 0
                for i in sum_out:
                    sum = sum + i
                ave = sum / len(sum_out)
                f.write("ave:" + str(ave) + '\n')
                f.write("时间:" + str(datetime.now()) + '\n')
                # sleep(5)
                APKmem_D2()
        except Exception as e:
            print(e)

def APKmem_D2():
    sum_out = []
    for number in range(1, 1):
        try:
            output = os.popen("adb shell dumpsys meminfo|findstr com.moredian.entrance.guard ").read()
            # print(output[3:9])
            RAM = int(output[3:output.find('kB') - 1])
            # print(RAM)
            with open(path + r'\meminfo-apk.txt', 'a+') as f:  # 设置文件对象
                f.write("Free RAM:" + str(RAM) + 'KB' + '\n')
                sum_out.append(RAM)
                sum = 0
                for i in sum_out:
                    sum = sum + i
                ave = sum / len(sum_out)
                f.write("ave:" + str(ave) + '\n')
                f.write("时间:" + str(datetime.now()) + '\n')
                # sleep(5)
                Temp_D2()
        except Exception as e:
            print(e)

def Temp_D2():
    io_array = []
    try:
        for i in range(1):
            f2 = open( path + r'\D2_temp.txt', 'a')
            output = os.popen('adb shell cat /sys/class/thermal/thermal_zone1/temp ')
            io = output.read()
            # print(int(io)/1000)
            temp = float(io)/1000
            io_array.append(temp)
            f2.write(str(temp) + '℃' + '\n')
        # print(" APK占用CPU：" + str(round(sum(io_array) / len(io_array), 2)) + "℃(" + str(
        #     round(max(io_array), 2)) + "℃-" + str(round(min(io_array), 2)) + "℃)")
            f2.write(" 平均温度：" + str(round(sum(io_array) / len(io_array), 2)) + "℃(" + str(
            round(max(io_array), 2)) + "℃-" + str(round(min(io_array), 2)) + "℃)"+'\n')
            f2.close()
    except Exception as e:
        print(e)

def chain():
    os.popen('adb logcat -s TrackTime >' + path + r'\TrackTime.txt')
    CPU_D2()
    # sleep(5)
    # os.popen('adb kill-server')
    pid_adb = os.popen('tasklist | findstr "adb"').read()
    pid_cmd = os.popen('tasklist | findstr "cmd"').read()
    # print(pid_adb[str(pid_adb).find("adb")+29:str(pid_adb).find("Console")-1])
    pid_adb = pid_adb[str(pid_adb).find("adb")+29:str(pid_adb).find("Console")-1]
    pid_cmd = pid_adb[str(pid_cmd).find("cmd") + 29:str(pid_cmd).find("Console") - 1]
    os.popen("taskkill /pid " + pid_adb + " -f")
    os.popen("taskkill /pid " + pid_cmd + " -f")




path = r"C:\Users\86183\Desktop\logs\logs"
# CPU_D2()
# APK_cpu_D2()
# Sysmem_D2()
# APKmem_D2()
# Temp_D2()
chain()