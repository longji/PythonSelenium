# Author:JiLong
from selenium import webdriver
from selenium.webdriver.common.by import By


#创建浏览器驱动对象
driver = webdriver.Chrome()
driver.get('file:///E:/workspase/pythonProject/PythonSelenium/SeleniumFoundation/Foundation/day1/test.html')

tetEle = driver.find_element(By.ID,'a')
# 获取元素属性值
print(tetEle.get_attribute('name'))


# 关闭浏览器
driver.quit()