# Author:JiLong
from selenium import webdriver


#创建浏览器驱动对象
driver = webdriver.Chrome()
driver.get('file:///E:/workspase/pythonProject/PythonSelenium/SeleniumFoundation/Foundation/day1/test.html')

# 先匹配到外层元素
txtEle = driver.find_element_by_tag_name('table')
# 在根据外层元素匹配里边的子元素
print(txtEle.find_element_by_tag_name('td').text)


# 关闭浏览器
driver.quit()