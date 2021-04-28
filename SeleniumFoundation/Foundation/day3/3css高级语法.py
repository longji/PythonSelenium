from selenium import webdriver


'''
优先级最高：id
优先级其次：name
优先级再次:css选择器
优先级再次：xpath

项目中用到最多的是css和xpath
一般来说，优先选择css
1.css配合HTML工作，它的实现原理是匹配对象。xpath是配合xml工作，实现原理是遍历
2.语言，相对于xpath来说更简洁
3.前端开发更主要用css，所以可以获得更多的帮助

'''
# 创建一个浏览器驱动
driver = webdriver.Chrome()
# 访问网址
driver.get("file:///F:/Users/JiLong/PycharmProjects/PythonSelenium/SeleniumFoundation/Foundation/day3/test.html")

# 元素定位的时候，不允许在by_class_name中出现空格，或以点代替空格
# 在css选择器定位的时候，运行以点代替空格
print(driver.find_element_by_css_selector('.ab2').text)



# 关闭浏览器
driver.quit()