from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost:8088/login")

class LoginPage:
    def __init__(self,driver):
        # 创建driver对象
        self.driver = driver

    def usernameBox(self):
        return self.driver.find_element_by_id("username")

    def passwordBox(self):
        return self.driver.find_element_by_name("password")

    def loginButtonBox(self):
        return self.driver.find_element_by_css_selector("div.login-wrap > button")

    def login(self):
        self.usernameBox().send_keys("libai")
        self.passwordBox().send_keys("opmsopms123")
        self.loginButtonBox().click()

class HomePage:
    def __init__(self,driver):
        # 创建driver对象
        self.driver = driver
    # 我的主页
    def myHomeBox(self):
        return self.driver.find_element_by_css_selector("i[class =\"fa fa-home\"] + span")
    # 项目管理
    def projectManagementBox(self):
        return self.driver.find_element_by_css_selector("i[class=\"fa fa-book\"] + span")

'''
陈旧元素：
1.定位元素，赋值给变量
2.界面刷新
3.调用变量操作元素，报错陈旧的元素
'''

if __name__ == '__main__':
    lp = LoginPage(driver)
    lp.login()
    hp = HomePage(driver)
    hp.myHomeBox().click()
    hp.projectManagementBox().click()
    hp.myHomeBox().click()