# Author:JiLong
from selenium import webdriver
from time import sleep


# 创建浏览器驱动对象
driver =webdriver.Chrome()
# 访问网址
driver.get('https://www.baidu.com/')

ele = driver.find_element_by_id('kw')
# 往文本框里面输入内容
ele.send_keys('绥德')
sleep(3)
# 清除文本框内容
ele.clear()
sleep(3)

ele.send_keys('绥德')
sleep(3)
# 点击元素
driver.find_element_by_id('su').click()
sleep(3)


# 关闭浏览器
driver.quit()