# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问地址
driver.get("https://www.baidu.com/")
driver.implicitly_wait(10)


# 搜索刘强东
driver.find_element_by_id('kw').send_keys('刘强东\n')
# 点击第一个链接
driver.find_element_by_css_selector(r'div[id="content_left"] > div:nth-child(1)> h3[class="t c-gap-bottom-small"] > a').click()

# 获取当前所有打开的窗口的句柄
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == "刘强东_百度百科":
        break

# 获取某元素的文本
txt = driver.find_element_by_css_selector("dl[class=\"second-know \"] >dt").text
print(txt)


# 关闭浏览器
driver.quit()