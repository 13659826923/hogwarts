from time import sleep
from appium import webdriver
from ez_setup import use_setuptools
desired_caps = {}
desired_caps['platformName']='Android'
#desired_caps['platformVersion']='6.0.1'
#desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.tencent.wework'
desired_caps['appActivity']='.lunch.LaunchSpalashActivity'
desired_caps["noReset"]="true"
desired_caps["ensureWebviewsHavePages"] = True
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

sleep(3)

driver.quit()

# 需要打开模拟器的调试模式，然后cmd执行这个命令 adb connect 127.0.0.1:7555 连上模拟器