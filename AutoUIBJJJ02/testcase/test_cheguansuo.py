# -*- coding: utf-8 -*-
# @Time : 2020/5/26 17:27
# @Author : 秦俊伟
# @Function:车管所业务测试用例执行

import os
import sys
rootpath=str(r"/root/.jenkins/workspace/BJJJ/AutoUIBJJJ02")
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)

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