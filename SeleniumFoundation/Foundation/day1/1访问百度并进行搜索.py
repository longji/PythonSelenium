# Author:JiLong
from selenium import webdriver
from time import sleep


#创建浏览器驱动对象
driver = webdriver.Chrome()

#访问百度网址
driver.get('https://www.baidu.com/')
#找到搜索输入框
inpEle = driver.find_element_by_id('kw')
inpEle.send_keys('特朗普')
#找到搜索按钮
driver.find_element_by_id('su').click()
sleep(5)

#关闭浏览器
driver.quit()