# -*-coding:utf-8-*-
from selenium import webdriver
import win32com.client
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 访问地址
driver.get("https://tinypng.com/")
'''
对于input 标签实现的上传功能，可将其看作是一个文本输入框
直接通过send_keys 指定本地文件路径实现文件上传
'''
driver.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\JiLong\\23.png")


'''
对于非input 标签实现的上传功能，我们可以通过模拟键盘敲击方式实现
'''
# 触发文件上传
# driver.find_element_by_css_selector(".target > .icon").click()
# sleep(10)
# sh =win32com.client.Dispatch("WScript.shell")
# sh.Sendkeys("C:\\Users\JiLong\\23.png\n")
