# Author:JiLong
from selenium import webdriver


# 创建一个浏览器驱动
driver = webdriver.Chrome()
# 访问网址
driver.get('https://www.baidu.com/')

# 用于获取当前页面的标题
print(driver.title)

# 找到搜索输入框
txtEle = driver.find_element_by_id('kw')
txtEle.send_keys('绥德')
# 找到搜索按钮
driver.find_element_by_id('su').click()

# 用于获取当前页面的url
print(driver.current_url)

# 获取元素的属性值
ele = driver.find_element_by_id('su')
print(ele.get_attribute('value'))

# 获取元素的文本信息，获取的是标签对中间的文本信息
ele = driver.find_element_by_css_selector('#s_tab > div > a.s-tab-item.s-tab-video')
print(ele.text)

# 关闭浏览器
driver.quit()