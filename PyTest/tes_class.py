import os
from time import sleep

from appium import webdriver


# server 启动参数
desired_capabilities = {}
# 设备信息
desired_capabilities['platformName'] = 'Android'
# desired_caps['platformVersion'] = '13'
desired_capabilities['deviceName'] = '192.168.3.27:39349'
# # app的信息
desired_capabilities['appPackage'] = 'com.alibaba.android.rimet'
desired_capabilities['appActivity'] = 'com.alibaba.android.rimet.biz.LaunchHomeActivity'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)


os.popen("adb shell input tap 560 1780")
sleep(3)
os.popen("adb shell input tap 311 2170")
sleep(3)
os.popen("adb shell input text '19106767703'")

# driver.find_element(str = "e67dab9c-c42e-4048-b4b7-0e7b8b0bb5dd",value="下一步").click()