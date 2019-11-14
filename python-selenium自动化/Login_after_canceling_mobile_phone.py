import sys

from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://10.10.8.2")
username = "2017214320"
password = "wang865931344"
driver.maximize_window()
#查找用户名
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys(username)
#查找密码
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(password)
#先注销
driver.find_element_by_class_name("a.a_demo_two").click()#注销
#driver.find_element_by_class_name("a.a_demo_two").click()#注销
time.sleep(0.5)
alert = driver.switch_to.alert #切换到alert
print('alert text : ' + alert.text) #打印alert的文本
alert.accept()
time.sleep(0.01)
driver.find_element_by_class_name("a.a_demo_one").click()#登陆
time.sleep(0.01)
driver.quit()
print("手机端连接已断开，电脑端连接成功")
os._exit(0)
