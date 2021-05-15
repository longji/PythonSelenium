'''
如果所有的父类都有相同的一个方法
继承顺序：1.先找自己 2.根据代码当中继承的父类顺序查找
'''
class Music_Player:
    def player(self):
        print('正在使用网易云音乐播放音乐')

    def call(self):
        print("使用老年机001正在打电话")

class Play_Games:
    def games(self):
        print('正在使用华为手机打游戏')

    def call(self):
        print("使用老年机002正在打电话")

class Phone:
    property = '杭州惠吧科技有限公司'
    def call(self):
        print("使用老年机003正在打电话")

    def send_short_messages(self):
        print('使用老年机正在发送短信')


class SmartPhone(Phone,Music_Player,Play_Games):
    # def call(self):
    #     self.video()
    #     print('使用智能手机正在打电话')
    def video(self):
        print('使用智能手机正在视频')

smart = SmartPhone()
smart.call()