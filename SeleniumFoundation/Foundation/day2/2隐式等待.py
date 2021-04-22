# Author:JiLong
from selenium import webdriver


# 创建一个浏览器驱动对象
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# 访问地址
driver.get('https://www.baidu.com')



# 关闭浏览器
driver.quit()