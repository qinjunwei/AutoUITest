# -*- coding: utf-8 -*-
# @Time : 2020/6/2 15:29
# @Author : 秦俊伟
# @Function:随手拍测试用例
from AutoUIBJJJ02.page.app import App

class TestSuiShouPai:
    def setup(self):
        self.home_page = App.start()

    def test_shipin(self):
        suishoupai_page = self.home_page.to_suishoupai()
        suishoupai_page.weifajubao()

    def test_tupian(self):
        pass

    def teardown(self):
        App.close()