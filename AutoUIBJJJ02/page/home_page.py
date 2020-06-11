# -*- coding: utf-8 -*-
# @Time : 2020/5/26 16:35
# @Author : 秦俊伟
# @Function:首页page
from selenium.webdriver.common.by import By
from AutoUIBJJJ02.page.base_bage import BasePage
from AutoUIBJJJ02.page.cheguansuo_page import CheGuanSuoPage
from AutoUIBJJJ02.page.suishoupai_page import SuiShouPaiPage
from AutoUIBJJJ02.utils.utils import Utils

class HomePage(BasePage):
    _cheguansuo_locat = (By.XPATH, "//*[@text='掌上车管所']")
    _suishoupai_locat = (By.XPATH, "//*[@text='随手拍']")
    #车管所模块
    def to_cheguansuo(self):
        Utils.click_tongyi(self.driver)
        self.find_element_click(self._cheguansuo_locat)
        return CheGuanSuoPage(self.driver)
    #随手拍模块
    def to_suishoupai(self):
        Utils.click_tongyi(self.driver)
        self.find_element_click(self._suishoupai_locat)
        return SuiShouPaiPage(self.driver)