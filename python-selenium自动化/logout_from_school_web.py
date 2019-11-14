import os
import sys

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://10.10.8.2")
username = "2017214320"
password = "wang865931344"
#driver.maximize_window()最大化窗口
#查找用户名
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys(username)
#查找密码
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(password)
#注销
driver.find_element_by_class_name("a.a_demo_two").click()#注销
driver.close()
print("连接已断开")
sys.exit(0)
