import random

def Temp():
    Temp_list=[]
    try:
        fopen = open(road + r'\temp.log',encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            Temp_Demo = lines[:-1]
            # print(Temp_Demo)
            Temp_list.append(int(Temp_Demo))
        fopen.close()
        # print(max(Temp_list)/1000)
        # print(min(Temp_list)/1000)
        # print(round((sum(Temp_list)/len(Temp_list))/1000,2))
        print("温度：" + str(round((sum(Temp_list)/len(Temp_list))/1000,2))+"℃("+str(min(Temp_list)/1000)+"℃-"+str(max(Temp_list)/1000)+"℃)")
    except Exception as e:
        print(e)

def systemMonitor():
    systemMonitor_list=[]
    try:
        fopen = open(road + r'\systemMonitor.log',encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "Start" not in str(lines) and "swap" not in str(lines) and "swpd" not in str(lines):
                free = lines[14:19]
                buff = lines[20:26]
                cache = lines[27:33]
                systemMonitor_Demo = int(free) + int(buff) + int(cache)
                # print(systemMonitor_Demo)
                systemMonitor_list.append(int(systemMonitor_Demo))
        fopen.close()
        # print(max(systemMonitor_list))
        # print(min(systemMonitor_list))
        # print(round((sum(systemMonitor_list)/len(systemMonitor_list)),2))
        print("剩余内存：" + str(
            round((sum(systemMonitor_list) / len(systemMonitor_list)), 2)) + "KB(" + str(min(systemMonitor_list)) + "KB-" + str(max(systemMonitor_list)) + "KB)")
    except Exception as e:
        print(e)

def guardMonitor():
    guardMonitor_list = []
    try:
        fopen = open(road + r'\guardMonitor.log', encoding='UTF-8')  # 设置文件对象
        for lines in fopen.readlines():
            if "Start" not in str(lines) and "com.moredian" in str(lines):
                guardMonitor_Demo = lines[lines.find("M")+8:lines.find("M")+13]
                # print(guardMonitor_Demo)
                guardMonitor_list.append(float(guardMonitor_Demo)/6)
        fopen.close()
        # print(max(guardMonitor_list))
        # print(min(guardMonitor_list))
        # print(round((sum(guardMonitor_list) / len(guardMonitor_list)), 2))
        print("apk的CPU占用率：" + str(
                round((sum(guardMonitor_list) / len(guardMonitor_list)), 2)) + "%(" + str(min(guardMonitor_list)) + "%-" + str(round(max(guardMonitor_list),2)) + "%)")
    except Exception as e:
        print(e)


road = r'C:\Users\86183\Desktop\stability\data'
Temp()
systemMonitor()
guardMonitor()