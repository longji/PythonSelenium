# 华为商城
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# 创建浏览器驱动
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 访问网址
driver.get('https://www.vmall.com/')

# 获取一级菜单下包含那些二级菜单
# 获取所有的一级菜单
liSli = driver.find_elements_by_xpath('//ol/li')
for li in liSli:
    # 一级菜单
    print("一级菜单:",li.find_element_by_xpath("./div[1]//span").text)
    # 鼠标悬停到一级菜单
    ActionChains(driver).move_to_element(li).perform()
    # 匹配到每一个二级菜单
    li2Sli = li.find_elements_by_xpath("//ol/li/div[2]//li[@class=\"subcate-item\"]")
    for li2 in li2Sli:
        print('\t',li2.text)

# 热销商品(向下滚动)
driver.execute_script("window.scrollBy(0,1000)")
# 找到每一个单品div.b clearfix > div.span-968 fl > ul > li.grid-items
liSli1 = driver.find_elements_by_css_selector("div.span-968.fl > ul.grid-list.clearfix > li.grid-items")
for li in liSli1:
    # 判断标题元素是否存在
    if li.find_elements_by_xpath(".//span"):
        # 获取商品名称
        goodName = li.find_element_by_xpath(".//div[@class=\"grid-title\"]")
        goodPace = li.find_element_by_xpath(".//p[@class=\"grid-price\"]")
        print('商品名称:{},价格:{}'.format(goodName.text,goodPace.text))



# 关闭浏览器
driver.quit()