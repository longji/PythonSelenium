# Author:JiLong
from selenium import webdriver


#创建浏览器驱动对象
driver = webdriver.Chrome()
driver.get('file:///E:/workspase/pythonProject/PythonSelenium/SeleniumFoundation/Foundation/day1/test.html')

# 根据class属性定位
tetEle = driver.find_elements_by_class_name('c')
print(tetEle[0].text)
# 退出浏览器
driver.quit()