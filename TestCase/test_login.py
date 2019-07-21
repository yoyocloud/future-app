#coding=utf-8
from PageObject.login_page import loginPage
from PageDatas.login_datas import loginDatas as ld
import pytest

# class TestLogin:

# @pytest.mark.parametrize("data",ld.right_info)
@pytest.mark.usefixtures("access_web")
@pytest.mark.smoke
def test_loginSucess(access_web):
    lp=loginPage(access_web)

    lp.login_username(ld.right_info["username"])
    lp.login_pwd(ld.right_info["pwd"])

    print("llllllllllllll")

