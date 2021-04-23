# Author:JiLong
from selenium import webdriver


# 创建一个浏览器驱动对象
driver = webdriver.Chrome()

# 设置隐私等待，只对之后的元素定位有效
# 隐私等待默认单位是秒
# 当代码执行到某个元素定位的时候，能找到元素就继续执行，如果找不到元素，就以轮询的方式不断定位
driver.implicitly_wait(10)

# 访问地址
driver.get('https://www.baidu.com')



# 关闭浏览器
driver.quit()