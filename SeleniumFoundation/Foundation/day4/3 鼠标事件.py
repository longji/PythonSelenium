# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问地址
driver.get("file:///F:/Users/JiLong/PycharmProjects/PythonSelenium/SeleniumFoundation/Foundation/day4/test2.html")


element1 = driver.find_element_by_id("blackSquare")
element2 = driver.find_element_by_id("targetEle")
# 鼠标拖拽
ActionChains(driver).drag_and_drop(element1,element2).perform()
sleep(3)
# 右击
ActionChains(driver).context_click(element1).perform()
# 双击
ActionChains(driver).double_click(element2).perform()
# 鼠标悬停
ActionChains(driver).move_to_element(element1).perform()
# 左键单击
ActionChains(driver).click(element1).perform()




# 关闭浏览器
driver.quit()