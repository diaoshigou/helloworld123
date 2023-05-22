# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import appium
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

TouchAction(driver).tap(x=163, y=890).perform()
TouchAction(driver).tap(x=141, y=890).perform()
TouchAction(driver).tap(x=716, y=646).perform()
TouchAction(driver).tap(x=928, y=657).perform()
TouchAction(driver).tap(x=309, y=1737).perform()
TouchAction(driver).tap(x=754, y=2095).perform()
TouchAction(driver).tap(x=331, y=1764).perform()
TouchAction(driver).tap(x=744, y=1970).perform()
TouchAction(driver).tap(x=961, y=1753).perform()
TouchAction(driver).tap(x=586, y=2220).perform()
TouchAction(driver).tap(x=754, y=1937).perform()
TouchAction(driver).tap(x=331, y=2089).perform()
TouchAction(driver).tap(x=347, y=2073).perform()
TouchAction(driver).tap(x=950, y=1758).perform()
TouchAction(driver).tap(x=722, y=1899).perform()
TouchAction(driver).tap(x=239, y=2062).perform()
TouchAction(driver).tap(x=364, y=2046).perform()
TouchAction(driver).tap(x=586, y=2236).perform()
TouchAction(driver).tap(x=722, y=1710).perform()
TouchAction(driver).tap(x=494, y=857).perform()
TouchAction(driver).tap(x=125, y=1259).perform()
TouchAction(driver).tap(x=374, y=885).perform()
TouchAction(driver).tap(x=98, y=1585).perform()
TouchAction(driver).tap(x=92, y=1596).perform()
TouchAction(driver).tap(x=765, y=2263).perform()
TouchAction(driver).tap(x=483, y=1406).perform()
TouchAction(driver).tap(x=385, y=857).perform()
TouchAction(driver).tap(x=152, y=890).perform()
TouchAction(driver).tap(x=526, y=2241).perform()
TouchAction(driver).tap(x=136, y=1742).perform()
TouchAction(driver).tap(x=575, y=467).perform()
TouchAction(driver).tap(x=336, y=1672).perform()

driver.quit()