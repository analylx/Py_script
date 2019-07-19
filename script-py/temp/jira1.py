#coding=utf-8
from selenium import webdriver
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class TestLogin(unittest.TestCase):
# 指定浏览器
    def setUp(self):
        self.driver = driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
        self.driver.get("https://147.234.236.106:8443/login.jsp")

    # 登录操作
    def test_login(self):
        title = self.driver.title
        print title
        now_url = self.driver.current_url
        print now_url
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
        # 登录成功断言
        login_name = self.driver.find_element_by_xpath('html/body/div[3]/div[2]/ul/li[1]/a/strong').text
        login_name = login_name.strip('您好：')
        assert login_name == username

    # 关闭浏览器
    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()