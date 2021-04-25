# Author:JiLong
from selenium import webdriver


# 创建一个浏览器驱动
driver = webdriver.Chrome()
# 访问微博热搜地址
driver.get('https://m.weibo.cn/')
driver.implicitly_wait(10)
# 点击大家都在搜
driver.find_element_by_xpath('//div[@class="m-text-cut"]').click()
# 点击微博热搜榜
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div/div[8]/div/div/h4').click()
# 找到外层热搜
hotEle = driver.find_element_by_xpath('//div[@class="card card11"][1]/div/div')
# 匹配每一行热搜存到列表里
hotSli = hotEle.find_elements_by_xpath('.//div[@class="box-left m-box-col m-box-center-a"]')
# 迭代列表
for ele in hotSli:
    # 判断这一行热搜有没有图片标签
    iconSli = ele.find_elements_by_xpath('./span[2]/span[@class="m-link-icon"]/img')
    if iconSli:
        img = iconSli[0]
        # 获取src属性
        srcLink = img.get_attribute('src')
        # 判断热搜类型
        if 'hot' in srcLink:
            hotType = '热'
            # 获取热搜文本
            hotText = ele.find_element_by_xpath('./span[2]/span[1]').text
            print("{}{}".format(hotType,hotText))
        elif 'new' in srcLink:
            hotType = '新'
            # 获取热搜文本
            hotText = ele.find_element_by_xpath('./span[2]/span[1]').text
            print("{}{}".format(hotType, hotText))

# 关闭浏览器
driver.quit()