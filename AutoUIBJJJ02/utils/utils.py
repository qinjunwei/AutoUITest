# -*- coding: utf-8 -*-
# @Time : 2020/5/27 17:39
# @Author : 秦俊伟
# @Function:
import yaml
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import os

class Utils:
    #点击弹框
    def click_tongyi(driver):
        def load_tongyi(driver):
            tys = driver.find_elements_by_xpath("//*[@text='同意']")
            print(datetime.datetime.now())
            if len(tys)>=1:
                tys[0].click()
                return True
            else:
                return False
        try:
            WebDriverWait(driver,10).until(load_tongyi(driver))
        except:
            print("时间内未找到弹框")

    #从yaml文件中取数据
    def read_yaml(self,path):
        with open(path,'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data

if __name__ == "__main__":
    p = os.path.join(os.path.dirname(os.getcwd()), "data", "testcase_steps.yml")
    u = Utils()
    d = u.read_yaml(p)
    print(type(d),d)
    print(datetime.datetime.now())