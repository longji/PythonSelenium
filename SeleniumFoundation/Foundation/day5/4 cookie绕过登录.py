cookies=[{'domain': 'localhost',
          'httpOnly': False,
          'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
          'path': '/',
          'secure': False,
          'value': '1620876742'},
         {'domain': 'localhost',
          'httpOnly': False,
          'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
          'path': '/',
          'secure': False,
          'value': '1620876742'},
         {'domain': 'localhost',
          'httpOnly': True,
          'name': 'beegosessionID',
          'path': '/', 'secure': False,
          'value': '023047f6c37a2bfb4ee4cb3dfb15e0e8'}]


from selenium import webdriver



# 创建浏览器驱动
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 访问地址
driver.get("http://localhost:8088/login")

# 清除原有的 cookie
# driver.delete_all_cookies()
# 设置 cookie
for cook in cookies:
    driver.add_cookie(cook)
driver.refresh()


