# Author:JiLong
from selenium import webdriver
from time import sleep


# 创建浏览器驱动对象
driver =webdriver.Chrome()
# 访问网址
driver.get('https://www.baidu.com/')

# # 控制浏览器大小
# driver.set_window_size(450,600)
#
# # 设置全屏显示
# driver.maximize_window()
#
# # 设置最小化浏览器
# driver.minimize_window()
# sleep(3)


driver.get('https://weibo.com/login.php')
# 控制浏览器后退
driver.back()
sleep(3)
# 控制浏览器前进
driver.forward()
sleep(3)
# 刷新
driver.refresh()
sleep(3)



# 关闭浏览器
driver.quit()