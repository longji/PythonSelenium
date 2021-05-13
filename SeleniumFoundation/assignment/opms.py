import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# 创建浏览器驱动
driver = webdriver.Chrome()
# 访问地址
driver.get("http://localhost:8088/login")
driver.implicitly_wait(10)

# 输入用户名和密码
driver.find_element_by_id("username").send_keys("libai")
driver.find_element_by_name("password").send_keys("opmsopms123")

# 确认登录
driver.find_element_by_css_selector("div.login-wrap > button").click()

# 点击项目管理
driver.find_element_by_css_selector("i[class=\"fa fa-book\"] + span").click()
# 点击新项目按钮
driver.find_element_by_css_selector("div[class=\"pull-right\"] > a").click()
# 输入项目名称
driver.find_element_by_css_selector("div[class=\"col-sm-10\"] > input[name=\"name\"]").send_keys("测试项目{}".format(time.strftime("%Y-%m-%d %X"),time.localtime()))
# 输入项目别名
driver.find_element_by_css_selector("div[class=\"col-sm-10\"] > input[name=\"aliasname\"]").send_keys("测试项目{}".format(time.strftime("%Y-%m-%d %X"),time.localtime()))

# 开始日期
started = driver.find_element_by_css_selector("input[class=\"form-control dpd1\"]")
started.click()
started.send_keys(Keys.CONTROL,'a')
started.send_keys(Keys.BACK_SPACE)
started.send_keys('2021-05-14')
# 结束日期
ended = driver.find_element_by_css_selector("input[class=\"form-control dpd2\"]")
ended.click()
ended.send_keys(Keys.CONTROL,'a')
ended.send_keys(Keys.BACK_SPACE)
ended.send_keys('2021-05-18')

# 切换到iframe
eleIframe = driver.find_element_by_css_selector("iframe")
driver.switch_to.frame(eleIframe)
# 输入内容
driver.find_element_by_css_selector("body[class=\"ke-content\"]").send_keys("松勤测试项目内容")
# 切换到主界面
driver.switch_to.default_content()
# 点击保存按钮
driver.find_element_by_css_selector("button[class=\"btn btn-primary\"]").click()