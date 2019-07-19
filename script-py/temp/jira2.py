#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
import sys
reload(sys)
import time
sys.setdefaultencoding('utf-8')
class TestLogin(unittest.TestCase):
# 指定浏览器
    def setUp(self):
        self.driver = driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
        #self.driver.get("https://147.234.236.106:8443/login.jsp")
        self.driver.get("https://ilptlppjir01.ecitele.com:8443/secure/Tests.jspa")

    # 登录操作
    def test_login(self):
        title = self.driver.title
        #print title
        now_url = self.driver.current_url
        #print now_url
        username = "a322494"
        password = "fs9999Ana"
        # 执行登录操作
        #用户名的定位
        self.driver.find_element_by_id("login-form-username").clear()
        self.driver.find_element_by_id("login-form-username").send_keys(username)
        #密码的定位
        self.driver.find_element_by_id("login-form-password").clear()
        self.driver.find_element_by_id("login-form-password").send_keys(password)
        # 点击登录
        self.driver.find_element_by_id("login-form-submit").click()
        time.sleep(10)
        #gclick the create button
        # xxx.find_element_by_xpath(“//a[contains(@href, ‘logout’)]”)
        self.driver.find_element_by_id("ktm-new-testcase").click()
        #原来的class名字是用空格隔开的组合，取其中一个标志性的就可以。不能同时用
        #取出来之后提示无法点击，位置不对（chrome会始终选择中间位置）或者是被其他的挡住了？
        #换个按钮去点击，优化调试的手段
        #self.driver.find_element_by_class_name("ktm-test-case-more").click()
        #self.driver.find_element_by_link_text("Create test cases in bulk...").click()
        #create new case
        self.driver.find_element_by_class_name("ktm-transparent-field").send_keys("create a new case step by step")
        self.driver.find_element_by_name("CF-281").find_element_by_xpath("//a[@title='Yes']")

        self.driver.find_element_by_name("CF-263").find_element_by_xpath("//a[@title='Yes']")
        
        Select(driver.find_element_by_id("select-box-14-button")).select_by_visible_text("Yes")
        Select(driver.find_element_by_id("select-box-15-button")).select_by_visible_text("Stress")
        Select(driver.find_element_by_id("select-box-13-button")).select_by_visible_text("Yes")
        Select(driver.find_element_by_id("select-box-16-button")).select_by_visible_text("Sheng Fang")

        #save the new case
        self.driver.find_element_by_class_name("aui-button aui-button-primary ktm-save-button ng-scope").click()

    # 关闭浏览器
    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()