'''
广度优先
深度优先
'''
class A:
    def play(self):
        print('a')

class B(A):
    def play(self):
        print('b')

class C(A):
    def play(self):
        print('c')

class D(B,C):
    def play(self):
        print('d')

d = D()
d.play()
# 查找顺序
print(D.__mro__)