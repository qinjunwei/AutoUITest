# -*- coding: utf-8 -*-
# @Time : 2020/5/26 17:27
# @Author : 秦俊伟
# @Function:车管所业务测试用例执行
from time import sleep
from AutoUIBJJJ02.page.app import App

class TestCheGuanSuo:

    def setup(self):
        self.home_page = App.start()

    def test_fuqi(self):
        cheguansuo = self.home_page.to_cheguansuo()
        cheguansuo.yewuyuyue()

    def teardown(self):
        sleep(2)
        App.close()