# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep


# 创建浏览器驱动
driver = webdriver.Chrome()
driver.maximize_window()
# 访问地址
driver.implicitly_wait(10)
driver.get("https://www.51job.com/")


# 点击高级搜索
driver.find_element_by_css_selector(".more").click()
# 输入关键字python
driver.find_element_by_id("kwdselectid").send_keys("java")
# 地区选择杭州
driver.find_element_by_id("work_position_input").click()
# 点击取消默认选中的城市
driver.find_element_by_css_selector("#work_position_click_multiple_selected > span").click()
# 点击选中杭州
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
sleep(10)
# 点击确定按钮
driver.find_element_by_id("work_position_click_bottom_save").click()
# 职能类别 1.首先点击空白地方  2.计算机软件-高级软件工程师
driver.find_element_by_css_selector("div.rtit.r1").click()

driver.find_element_by_id("funtype_click").click()
driver.find_element_by_id('funtype_click_center_left_each_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()

# 公司性质 国企
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_css_selector('span[title="国企"]').click()

# 工作年限
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_css_selector('span[title="1-3年"]').click()

# 点击确认搜索
driver.find_element_by_css_selector('div.btnbox.p_sou > span.p_but').click()
sleep(5)

# 获取职位列表并打印
Position_list = driver.find_elements_by_css_selector('div.j_joblist > div.e')
for posttionlist in Position_list:
    position = posttionlist.find_element_by_css_selector('span[title]').text
    company = posttionlist.find_element_by_css_selector('a[title]').text
    region = posttionlist.find_element_by_css_selector('span.d.at').text
    salary = posttionlist.find_element_by_css_selector('span.sal').text
    print("|".join([position,company,region,salary]))

sleep(5)
# 退出浏览器
driver.quit()