# -*- coding: utf-8 -*-
# @Time : 2020/6/2 15:24
# @Author : 秦俊伟
# @Function:随手拍页面业务
from selenium.webdriver.common.by import By
from AutoUIBJJJ02.page.base_bage import BasePage


class SuiShouPaiPage(BasePage):
    _paishipin = (By.XPATH, "//*[@text='拍视频']")
    _shipinpaishe = (By.XPATH, "//*[@text='点击拍摄']")
    _quxiaopaishe = (By.XPATH, "//*[@text='取消拍摄']")

    def weifajubao(self):
        pass