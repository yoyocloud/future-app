from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction



desired_caps={}
#平台类型
desired_caps["platformName"]="Android"
#平台版本号
# desired_caps["platformVersion"]="4.4.2"
desired_caps["platformVersion"]="7.0"
#设备名称
# desired_caps["deviceName"]="Android Emulator"
desired_caps["deviceName"]="8FS5T16614006423"
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
#18684720553
#连接appium服务器，前提：appium desktop要启动，有监听端口
#将desired_caps发送给appium server。打开app
driver=Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_caps)
#
# loc='new UiSelector().text("全程班")'
# ele=WebDriverWait(driver,5).until(ec.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,loc)))
# ele.click()

# time.sleep(3)
#
# webview_ele="android.webkit.WebView"
# WebDriverWait(driver,5).until(ec.visibility_of_element_located((MobileBy.CLASS_NAME,webview_ele)))
#
# # print(driver.contexts)
# con=driver.contexts
#
# #切换
# driver.switch_to.context(con[-1])
#
# #等待+点击立即购买
# click_ele=WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,'//button[text()="立即购买"]')))
# click_ele.click()

time.sleep(5)
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

loc=(By.ID,"com.xxzb.fenwoo:id/btn_start")
try_ele=WebDriverWait(driver=driver,timeout=10).until(ec.presence_of_element_located(loc))
try_ele.click()