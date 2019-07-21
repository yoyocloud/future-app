#coding=utf-8
from Common.basepage import BasePage
from PageLocator.login_locator import loginLocator as ll

class loginPage(BasePage):


    #正常的登录成功
    def login_username(self,msg):
        #找元素输入框
        self.visibility_ele(ll.username_loc)
        #输入用户名
        self.input_text(msg=msg,loc=ll.username_loc)
        #点击下一步
        self.click_ele(ll.next_stop_loc)

    def login_pwd(self,msg):
        #z找到密码输入框
        self.visibility_ele(loc=ll.pwd_loc)
        #输入密码
        self.input_text(msg=msg,loc=ll.pwd_loc)
        #点击下一步
        self.click_ele(ll.sure_button_loc)

    # #输入错误的手机号码获取提示  两种情况空的 和错误的
    # def login_wrongUsername(self):
    #     pass
    # #输入错误的密码。两种情况 空的和错误的
    # def login_worngPwd(self):
    #     pass

