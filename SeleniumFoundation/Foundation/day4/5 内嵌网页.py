# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问地址
driver.get("file:///F:/Users/JiLong/PycharmProjects/PythonSelenium/SeleniumFoundation/Foundation/day4/test3.html")


# 内嵌函数
'''
1.定位到想进入的iframe标签
2.切换进去
3.切换主页面
'''
Embedded = driver.find_element_by_css_selector("iframe:nth-child(3)")
driver.switch_to.frame(Embedded)
driver.find_element_by_id("kw").send_keys("你好")
sleep(3)
# 切换到主页面
driver.switch_to.default_content()



# 关闭浏览器
driver.quit()