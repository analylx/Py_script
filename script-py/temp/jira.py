# -*- coding:utf-8 -*-
from selenium import webdriver
from time import *
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://147.234.236.106:8443/login.jsp")
sleep(6)
# 添加Cookie
driver.add_cookie({'name': 'a322494', 'value': '23D5710DC3108E0F29120B30A90D1718'})

# 刷新页面
driver.refresh()

#关闭浏览器
driver.quit()