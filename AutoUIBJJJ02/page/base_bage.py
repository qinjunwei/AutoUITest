# -*- coding: utf-8 -*-
# @Time : 2020/6/1 15:57
# @Author : 秦俊伟
# @Function:
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    #查找元素
    def find_element(self,locat):
        return self.driver.find_element(*(locat))

    #查找元素并点击
    def find_element_click(self,locat):
        self.find_element(locat).click()

    #多个元素
    def find_elements(self,locat):
        return self.driver.find_elements(*(locat))

    #多个元素并点击
    def find_elements_click(self,locat,index:int):
        self.find_elements(locat)[index].click()