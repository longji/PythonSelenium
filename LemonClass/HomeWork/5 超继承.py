class Phone:
    property = '杭州惠吧科技有限公司'
    def call(self):
        print("使用老年机正在打电话")

    def send_short_messages(self):
        print('使用老年机正在发送短信')


class SmartPhone(Phone):
    def call(self):
        # self.video()
        # print('使用智能手机正在打电话')

        # supper()就是调用父类的call()方法
        super().call()

    def video(self):
        print('使用智能手机正在视频')

smart = SmartPhone()
smart.call()