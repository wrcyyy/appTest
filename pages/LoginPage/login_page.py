# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 14:53
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : login_page.py
@IDE     : PyCharm
------------------------------------
"""
import allure
import os
from pages.pages import BasePageElements
from common.base import BaseOperation

current_dir = os.path.abspath(os.path.dirname(__file__))


class LoginPage(BaseOperation, BasePageElements):
    def __init__(self, driver):
        BaseOperation.__init__(self, driver)
        BasePageElements.__init__(self, '', 'Login.yml', current_dir)

    @allure.step('输入用户名')
    def send_username(self, username: str):
        self.send_key(self.locator("user_name"), username)

    @allure.step("清空用户名输入框")
    def clear_username_input_box(self):
        self.clear_input_box(self.locator("user_name"))

    @allure.step('输入密码')
    def send_password(self, password: str):
        self.send_key(self.locator("password"), password)

    @allure.step('点击登录按钮')
    def click_login_btn(self):
        self.click(self.locator("login_btn"))
