# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep


# 创建浏览器驱动
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 访问地址
driver.get('https://www.baidu.com/')


# 找到搜索输入框
Search = driver.find_element_by_id('kw')
Search.send_keys("绥德")
sleep(3)

# 删除一个字符，退格键
Search.send_keys(Keys.BACK_SPACE)


# 全选
Search.send_keys(Keys.CONTROL,'a')

'''
Keys.BACK_SPACE #删除键
Keys.SPACE #空格键
Keys.TAB #制表符
Keys.ESCAPE #回退键 Esc
Keys.CONTROL #control 键
Keys.SHIFT #Shift键
'''


# 关闭浏览器
driver.quit()