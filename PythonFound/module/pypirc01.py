# 多重继承
class A:
    def aa(self):
        print('aa')

    def say(self):
        print('say AAA')

class B:
    def bb(self):
        print('bb')

    def say(self):
        print('say BBB')

class C(B,A):
    def cc(self):
        print('cc')

c = C()
print(C.mro()) #打印类的层次
