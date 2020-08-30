import os

def CPU_D3():
    io_array = []
    for i in range(3):
        # f2 = open('D:\log\D2-D-cpu_static.txt', 'a')
        output = os.popen('adb shell top -n 1|findstr "cpu"')
        # print("第"+str(i)+"次")
        io = output.read()
        # f2.write(io)
        # print(io[io.find('sys')+4:io.find("idle")-1])
        io_array.append(800 - int(io[io.find('sys')+4:io.find("idle")-1]))
        # f2.close()
    print(" CPU总占用率：" + str(round((sum(io_array)/len(io_array))/8,2))+"%("+str(round(max(io_array)/8,2))+"%-"+str(round(min(io_array)/8,2))+"%"+')')

def APK_cpu_D2P():
    io_array = []
    for i in range(3):
        # f2 = open('D:\log\D2-D-cpu_static.txt', 'a')
        output = os.popen('adb shell top -n 1|findstr "com.moredian" ')
        # print("第"+str(i)+"次")
        io = output.read()
        # f2.write(io)
        # print(io[43:47])
        # print(type(float(io[43:47])))
        io_array.append(float(io[43:47]))
        # f2.close()
    print(" APK占用CPU：" + str(round(sum(io_array)/len(io_array),2))+"%("+str(round(max(io_array),2))+"%-"+str(round(min(io_array),2))+"%)")

CPU_D3()
# APK_cpu_D2P()