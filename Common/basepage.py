#utf-8
import appium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

class BasePage:
    def __init__(self,driver):
        self.driver=driver
    def visibility_ele(self,loc):
        try:
            return WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(loc))

        except:
            logging.info("等待元素可见出错了")
            raise

    def click_ele(self,loc):
        ele=self.visibility_ele(loc)
        try:
            ele.click()
        except:
            logging.info("点击元素失败")
            raise

    def input_text(self,loc,msg):
        ele = self.visibility_ele(loc)
        try:
            ele.send_keys(msg)
        except:
            logging.info("输入内容失败")
            raise

    pass
    def get_attr(self):
        pass
    def get_text(self):
        pass
