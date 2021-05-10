from selenium import webdriver


# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问百度
driver.get('https://www.baidu.com/')

# 截图，截取整个页面
driver.get_screenshot_as_file('./all.png')
# 截图，截取单个元素
Screenshot = driver.find_element_by_id('kw')
Screenshot.screenshot('./Screenshot.png')


# 退出浏览器
driver.quit()