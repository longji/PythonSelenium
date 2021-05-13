# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问地址
driver.get("file:///F:/Users/JiLong/PycharmProjects/PythonSelenium/SeleniumFoundation/Foundation/day5/test.html")


# 1.定位下拉框元素 select标签
ele = driver.find_element_by_id("abc")

#根据可视文本选择
# Select(ele).select_by_visible_text("月薪三十万")

#根据value属性选择
# Select(ele).select_by_value("p1")

#根据下标选择
# Select(ele).select_by_index(1)
# sleep(3)

# 关闭浏览器
driver.quit()