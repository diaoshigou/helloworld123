import subprocess
from time import sleep

# process = subprocess.Popen('adb shell am start com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity')
# sleep(2)
# tap_delete_number = subprocess.Popen('adb shell input tap 960 638',shell=True)
# sleep(2)
# input_number = subprocess.Popen('adb shell input text 19106767703')
# sleep(2)
# focus_password = subprocess.Popen('adb shell input tap 88 888',shell=True)
# sleep(2)
# input_password = subprocess.Popen('adb shell input text Fz6%La4D')
# sleep(2)
# input_argee = subprocess.Popen('adb shell input tap 117 1204',shell=True)
# sleep(2)
# input_login = subprocess.Popen('adb shell input tap 534 1000',shell=True)
# sleep(2)
# cancel_number_save = subprocess.Popen('adb shell input tap 645 2169',shell=True)
# sleep(2)
# Switch_pages = subprocess.Popen('adb shell input tap 540 2236',shell=True)

for i in range(1,10000):
    # tap_delete_number = subprocess.Popen('adb shell input tap 300 300', shell=True)
    # sleep(8)
    # input_number = subprocess.Popen('adb shell input tap 70 50')
    sleep(1)
    focus_password = subprocess.Popen('adb shell input tap 1200 300', shell=True)
    sleep(3)
    input_back = subprocess.Popen('adb shell input tap 70 50')
    sleep(1)
    i = i + 1
    print(i)