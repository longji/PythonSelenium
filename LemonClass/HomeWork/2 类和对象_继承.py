'''
1.类和对象的定义
2.类的对象的使用
3.属性，类属性，实例属性   类属性=类变量   实例属性=实例变量
4.方法，【实例方法】，静态方法，类方法
'''
# 类的继承
class Phone:
    property = '杭州惠吧科技有限公司'
    def call(self):
        print("使用老年机正在打电话")

    def send_short_messages(self):
        print('使用老年机正在发送短信')


class SmartPhone(Phone):
    def call(self):
        self.video()
        print('使用智能手机正在打电话')
    def video(self):
        print('使用智能手机正在视频')

smart = SmartPhone()
# smart.call()
# smart.send_short_messages()
# smart.video()
# print(smart.property)
smart.call()