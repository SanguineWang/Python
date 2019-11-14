import os
import sys

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://10.10.8.2")
username = "2017214320"
password = "wang865931344"
#driver.minimize_window()
#查找用户名
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys(username)
#查找密码
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(password)
#登录
time.sleep(1)
driver.find_element_by_class_name("a.a_demo_one").click()#登陆
#driver.find_element_by_name("password").send_keys(Keys.SPACE)#模拟回车
driver.quit()#关闭浏览器
print("连接成功")
sys.exit(0)