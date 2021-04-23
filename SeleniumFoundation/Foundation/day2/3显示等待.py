# Author:JiLong
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# 创建一个浏览器驱动对象
driver = webdriver.Chrome()

# 访问网址
driver.get('https://www.baidu.com')

# 显示等待，每隔0.5秒检查一次，最多等待10秒
WebDriverWait(driver,10,0.5).until(
    EC.visibility_of_element_located(
        (By.ID,'kw') #判断元素在界面上是否被加载出来
    )
)
driver.find_element_by_id('kw').send_keys('绥德')
driver.find_element_by_id('su').click()

# 关闭浏览器
driver.quit()