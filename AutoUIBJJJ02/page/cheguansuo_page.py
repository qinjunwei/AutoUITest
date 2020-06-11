# -*- coding: utf-8 -*-
# @Time : 2020/5/26 17:18
# @Author : 秦俊伟
# @Function:车管所业务page
from selenium.webdriver.common.by import By
from AutoUIBJJJ02.page.base_bage import BasePage

class CheGuanSuoPage(BasePage):
    _yw_locat = (By.ID, "tv_cgsyw")
    _fq_locat = (By.ID, "tv_item_content")
    _yyxz_locat = (By.ID, "tv_top")
    _xyb_locat = (By.ID, "tv_bottom")
    _xzcgs_locat = (By.XPATH, "//*[@text='车辆管理所京朝分所']")
    _xzrq_locat = (By.ID, "area_1")
    _tjyy_locat = (By.ID, "tv_sure")
    # _data = Utils.read_yaml()
    #     # @pytest.mark.parametrize("idcar, name1, idnumber1, name2, idnumber2, zjid", _data)
    def yewuyuyue(self):
        self.find_element_click(self._yw_locat)# 车管业务
        self.find_elements_click(self._fq_locat,8)# 夫妻业务
        self.find_element_click(self._yyxz_locat)# 预约须知底部勾选框
        self.find_element_click(self._xyb_locat)# 下一步
        self.find_element_click(self._xzcgs_locat)# 选择车管所
        self.find_elements_click(self._xzrq_locat,5)# 选择日期
        self.find_element_click(self._tjyy_locat)# 提交预约
        self.driver.get_screenshot_as_file(r"F:\a.png")