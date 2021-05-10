# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问地址
driver.get("file:///F:/Users/JiLong/PycharmProjects/PythonSelenium/SeleniumFoundation/Foundation/day4/test1.html")

# 触发对话框
# driver.find_element_by_id('bu1').click()
# dialogueframe = driver.switch_to.alert
# print(dialogueframe.text) #返回警告框内的信息
# dialogueframe.accept() #接受现有警告框
# sleep(3)

# 触发确认框
# driver.find_element_by_id('bu2').click()
# ConfirmFrame = driver.switch_to.alert
# ConfirmFrame.dismiss() #取消现有警告框
# sleep(3)

# 触发提示框
driver.find_element_by_id('bu3').click()
promptframe = driver.switch_to.alert
promptframe.send_keys('咸阳')
sleep(5)
promptframe.accept()
sleep(3)


# 关闭浏览器
driver.quit()