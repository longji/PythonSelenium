'''
多重继承，子类可以同时继承多个父类，这些父类的特性（属性，方法）子类都可以使用

class 子类名(父类1，父类2，...,父类n)
'''
class Music_Player:
    def player(self):
        print('正在使用网易云音乐播放音乐')

class Play_Games:
    def games(self):
        print('正在使用华为手机打游戏')

class Phone:
    property = '杭州惠吧科技有限公司'
    def call(self):
        print("使用老年机正在打电话")

    def send_short_messages(self):
        print('使用老年机正在发送短信')


class SmartPhone(Phone,Music_Player,Play_Games):
    def call(self):
        self.video()
        print('使用智能手机正在打电话')
    def video(self):
        print('使用智能手机正在视频')

smart = SmartPhone()
smart.player()
smart.games()
