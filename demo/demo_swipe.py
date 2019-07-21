#coding=utf-8
from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import time



desired_caps={}
#平台类型
desired_caps["platformName"]="Android"
#平台版本号
desired_caps["platformVersion"]="4.4.2"
#设备名称
desired_caps["deviceName"]="Android Emulator"
#app包名
# desired_caps["appPackage"]="com.lemon.lemonban"
#前程贷的包名com.xxzb.fenwoo
desired_caps["appPackage"]="com.xxzb.fenwoo"

#app入口activity
# desired_caps["appActivity"]="com.lemon.lemonban.activity.WelcomeActivity"
desired_caps["appActivity"]="com.xxzb.fenwoo.activity.addition.WelcomeActivity"
#前程贷的入口activity名称com.xxzb.fenwoo.activity.addition.WelcomeActivity
#是否重置
# desired_caps["noReset"]= True

#连接appium服务器，前提：appium desktop要启动，有监听端口
#将desired_caps发送给appium server。打开app
driver=Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_caps)

# loc=(MobileBy.ID,"com.lemon.lemonban:id/navigation_my")
# ele=WebDriverWait(driver,10,0.2).until(ec.visibility_of_element_located(loc))
# ele.click()
#uiautomator
# loc_ningmeng='new UiSelector.text("柠檬社区")'
# driver.find_element_by_android_uiautomator(loc_ningmeng)
#
# #content_desc的值
# driver.find_element_by_accessibility_id()
# #id
# driver.find_element_by_id()
# #class
# driver.find_element_by_class_name()

time.sleep(2)
#滑屏操作
#先获取窗口的大小
size=driver.get_window_size()

#左滑先确定到size的宽90宽50
star_x=size["width"]*0.9
star_y=size["height"]*0.5

end_x=size["width"]*0.1
end_y=size["height"]*0.5
# driver.swipe(star_x,star_y,end_x,end_y,duration=200)
for i in range(3):
    driver.swipe(star_x, star_y, end_x, end_y, duration=200)
    time.sleep(1)

#向右滑动

# driver.swipe(end_x,star_y,star_x,end_y,duration=200)
