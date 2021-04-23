# Author:JiLong
from selenium import webdriver


# 创建一个浏览器驱动对象
driver = webdriver.Chrome()
# 访问网址
driver.get('file:///E:/workspase/pythonProject/PythonSelenium/SeleniumFoundation/Foundation/day2/test.html')

elenium = driver.find_element_by_xpath('//tr[2]//td[3]')
print(elenium.text)


# 关闭浏览器
driver.quit()