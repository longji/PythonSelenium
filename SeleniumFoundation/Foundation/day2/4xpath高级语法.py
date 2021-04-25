# Author:JiLong
from selenium import webdriver


# 创建一个浏览器驱动对象
driver = webdriver.Chrome()
# 访问网址
driver.get('file:///E:/workspase/pythonProject/PythonSelenium/SeleniumFoundation/Foundation/day2/test.html')

elenium = driver.find_element_by_xpath("//tr//td[@id='a1']/..")
'''
//tr//td[@id='a1']/parent::tr #parent::等同于/.. 父元素
//tr//td[@id='a1']/ancestor-or-self::td #ancestor-or-self::*包含上下文节点本身和该节点的祖先节点
descendant 选取当前节点的后代元素
descendant-or-self 选取当前节点的后代元素以及当前节点本身

//td[@id="a2"]/preceding::td #preceding当前节点之前的
//td[@id="a1"]/following::td #following当前节点之后的
'''
print(elenium.find_element_by_xpath('./td[3]').text)


# 关闭浏览器
driver.quit()