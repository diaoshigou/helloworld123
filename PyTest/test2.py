import serial
import keyboard
#keyboard  模拟键盘操作
ser = serial.Serial("COM5",timeout=1) #打开串口,超时时间1s
ser.baudrate = 115200
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
if ser.is_open:
    print("成功打开串口")
    print(ser)
    keyboard.press('enter') #为防止命令无法输入，先模拟键盘点击enter键

    keyboard.release('enter')
    ser.write(b"free")
    # 读取命令执行结果值
    keyboard.press('enter')  # 为防止命令无法输入，先模拟键盘点击enter键

    keyboard.release('enter')
    ser.flush()
    response = ser.readlines()
    # 打印命令执行结果值
    print("命令执行结果值:", response)
    ser.close()
else:
    print("无法打开串口")