# -*- coding: utf-8 -*-
# @Time : 2020/5/26 16:37
# @Author : 秦俊伟
# @Function:App启动与App关闭
from appium import webdriver
from AutoUIBJJJ02.page.home_page import HomePage

class App:
    @classmethod
    def start(self):
        cps = {
            "platformName": "android",
            "deviceName": "qin",
            "appPackage": "com.zcbl.bjjj_driving",
            "appActivity": "com.zcbl.manager.MainActivity",
            # "platformVersion":"6.1.0",
            "automationName":"uiautomator2",
            "autoGrantPermissions": True,#自动处理权限
            "noReset": True,#不重置app相关环境
            "unicodeKeyboard":'true'#支持中文输入
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",cps)
        self.driver.implicitly_wait(15)
        return HomePage(self.driver)

    @classmethod
    def close(self):
        self.driver.quit()