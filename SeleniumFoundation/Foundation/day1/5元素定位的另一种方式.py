# Author:JiLong
from selenium import webdriver
from selenium.webdriver.common.by import By


#创建浏览器驱动对象
driver = webdriver.Chrome()
driver.get('file:///E:/workspase/pythonProject/PythonSelenium/SeleniumFoundation/Foundation/day1/test.html')

txtEle = driver.find_elements(By.CLASS_NAME,'c')
for i in txtEle:
    print(i.text)


# 关闭浏览器
driver.quit()