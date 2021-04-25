# Author:JiLong
from selenium import webdriver


# 创建浏览器驱动对象
driver =webdriver.Chrome()
# 访问网址
driver.get('https://www.baidu.com/')

# 控制浏览器大小
driver.set_window_size(450,600)




# 关闭浏览器
driver.quit()