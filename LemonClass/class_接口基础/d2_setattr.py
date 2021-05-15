'''
setattr:设置属性（动态获取某个属性的函数）
setattr(对象或者类，属性名称，赋值的新值)
setattr 不管属性存在不存在，都会赋给新值
'''

class Phone:
    property = True

    def __init__(self,brand):
        self.brand = brand

    def call(self):
        self.xianren = "男"
        print("使用老年机正在打电话")

    def send_short_messages(self):
        print('使用老年机正在发送短信')

iphone = Phone('xiaomi')
iphone.brand = 'apple'

# print(iphone.brand)


# 获取属性，获取属性如果不存在，则报错
# 修改，字典
# iphone.color = 'red'
# print(iphone.color)

# 有时候，提前不知道属性名称是什么，从其他地方拿过来
setattr(iphone, 'food', '麻辣烫')
print(iphone.food)


setattr(iphone,'brand','华为mate40pro')
print(iphone.brand)