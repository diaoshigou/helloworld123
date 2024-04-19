import subprocess
from time import sleep
import random

# process = subprocess.Popen('adb shell am start com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity')


for i in range(1,11):
    random_float = float(random.randrange(3, 6))
    print(random_float + round(random.random(), 2))

#
# for i in range(3.000,5.000):
#     # tap_delete_number = subprocess.Popen('adb shell input tap 300 300', shell=True)
#     # sleep(8)
#     # input_number = subprocess.Popen('adb shell input tap 70 50')
#     j= 1
#     if j < 20:
#         print(float(i))