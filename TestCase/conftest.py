#coindg=utf-8
import pytest
from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def access_web():

    desired_caps = {}
    # 平台类型
    desired_caps["platformName"] = "Android"
    # 平台版本号
    desired_caps["platformVersion"] = "7.0"
    # 设备名称
    desired_caps["deviceName"] = "8FS5T16614006423"
    # app包名
    # desired_caps["appPackage"]="com.lemon.lemonban"
    # 前程贷的包名com.xxzb.fenwoo
    desired_caps["appPackage"] = "com.xxzb.fenwoo"

    # app入口activity
    # desired_caps["appActivity"]="com.lemon.lemonban.activity.WelcomeActivity"
    desired_caps["appActivity"] = "com.xxzb.fenwoo.activity.addition.WelcomeActivity"
    desired_caps["noReset"]=True
    driver = Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)

    time.sleep(2)
    # 滑屏操作
    # 先获取窗口的大小
    # size = driver.get_window_size()
    #
    # # 左滑先确定到size的宽90宽50
    # star_x = size["width"] * 0.9
    # star_y = size["height"] * 0.5
    #
    # end_x = size["width"] * 0.1
    # end_y = size["height"] * 0.5
    # # driver.swipe(star_x,star_y,end_x,end_y,duration=200)
    # for i in range(3):
    #     driver.swipe(star_x, star_y, end_x, end_y, duration=200)
    #     time.sleep(1)
    # time.sleep(4)
    # #立即体验
    # loc=(By.ID,"com.xxzb.fenwoo:id/btn_start")
    # print("kkkkkkkkk")
    # WebDriverWait(driver,10).until(ec.presence_of_element_located(loc)).click()
    # print("ssssssss")

    #注册/登录
    loc=(MobileBy.ID,"com.xxzb.fenwoo:id/btn_login")
    WebDriverWait(driver,10).until(ec.visibility_of_element_located(loc)).click()

    yield driver

