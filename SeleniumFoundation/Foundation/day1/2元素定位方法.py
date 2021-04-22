# Author:JiLong
from selenium import webdriver


'''
选择界面元素
根据元素的特征选择：ID，Name，Class，TagName，link_text
根据元素的特征和关系选择：css，xpath

操作界面元素
输入操作：点击、输入文字、拖拽等
输出操作：获取元素的各种属性
'''
#创建浏览器驱动对象
driver = webdriver.Chrome()
driver.get('file:///E:/workspase/pythonProject/PythonSelenium/SeleniumFoundation/Foundation/day1/test.html')

# 通过ID属性定位
# tetEle = driver.find_element_by_id('a')
# 获取元素文本值
# print(tetEle.text)

# 通过name属性定位
# tetEle = driver.find_element_by_name('b')
# print(tetEle.text)

# 通过xpath属性定位
# tetEle = driver.find_element_by_xpath('/html/body/input')
# tetEle.send_keys('遥看是君家，松柏冢累累')

# 通过css定位
# tetEle = driver.find_element_by_css_selector('body > p:nth-child(4)')
# print(tetEle.text)

# 根据连接文本定位，精准搜索
# driver.find_element_by_link_text('百度一下，你就知道').click()
# 根据连接文本定位，模糊搜索
# driver.find_element_by_partial_link_text('百度一下').click()

# 跟进tag_name定位
# tetEle = driver.find_element_by_tag_name('p')
# print(tetEle.text)

# 根据class属性定位
tetEle = driver.find_element_by_class_name('c')
print(tetEle.text)
# 退出浏览器
driver.quit()