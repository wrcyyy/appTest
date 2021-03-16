# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : appTest
@Time    : 2021/3/16 14:41
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : conftest.py
@IDE     : PyCharm
------------------------------------
"""

import logging
import pytest
from appium import webdriver


@pytest.fixture(scope='session')
def login_app():
    capabilities = {
        # 手机系统类型 Android or ios
        'platformName': 'Android',
        # 手机系统版本
        'platformVersion': '9',
        # 手机名称
        'deviceName': 'V1813BT',
        # 'systemPort': conf.devices['systemPort'],
        # app的appActivity名
        'appActivity': 'cn.com.smartfleet.app.admin.MainActivity',
        # app的包名
        'appPackage': 'cn.com.smartfleet.app.admin',
        'automationName': 'UIAutomator2',
        'clearSystemFiles': True,
        'noSign': True,
        'recreateChromeDriverSessions': True,
        "unicodeKeyboard": True,
        "noReset": True,
        "fullReset": False,
        "newCommandTimeout": 6000,
        'resetKeyboard': True,
        'skipServerInstallation': True  # 手机跳过uiAutomator2服务器的安装
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    driver.implicitly_wait(10)
    yield driver
    driver.close_app()
    driver.quit()
