from selenium import webdriver
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 访问地址
driver.get("http://localhost:8088/login")


# 获取登录前的cookie信息
# cook = driver.get_cookies()
# 打印cookie信息
# print(cook)
# print(driver.get_cookie('Hm_lpvt_750463144f16fe69eb3ac11bea1c4436'))

# 登录后的cookie信息
driver.find_element_by_id("username").send_keys("libai")
driver.find_element_by_name("password").send_keys("opmsopms123")
driver.find_element_by_css_selector("div.login-wrap > button").click()


cooks = driver.get_cookies()
print(cooks)