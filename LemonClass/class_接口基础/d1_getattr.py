'''
getattr:获取属性（动态获取某个属性的函数）
getattr(对象或者类，属性名称，当么此属性的时候提供的默认值)
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
# print(iphone.brand) #xiaomi
# print(iphone.xianren) #AttributeError: 'Phone' object has no attribute 'xianren'

# print(getattr(iphone, 'xianren','女'))
# print(getattr(iphone, 'brand', 'huawei')) #xiaomi

# 类名.类属性    类名.实例属性（错误）
# print(getattr(Phone, 'brand', '苹果')) #苹果

print(getattr(Phone, 'property', '杭州西湖')) #True