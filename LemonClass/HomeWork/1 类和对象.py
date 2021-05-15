'''
1.编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算
'''
# class Computing:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#
#     def addition(self):
#         return self.a+self.b
#
#     def subtraction(self):
#         return self.a-self.b
#
#     def multiplication(self):
#         return self.a*self.b
#
#     def division_method(self):
#         try:
#             return self.a / self.b
#         except BufferError as e:
#             print(e)
#
#
# call = Computing(4,0)
# print(call.division_method())


'''
2.定义一个手机类，具有打电话和录音的功能，打电话的时候可以录音，也可以不录音
'''
class Phone:
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def call(self,recode):
        if recode == True:
            self.record()
        print('打电话')

    def record(self):
        print("{}的{}正在进行录音".format(self.color,self.model))

    def __repr__(self):
        '''返回对象打印出来的效果'''
        return self.model

iphome = Phone('华为Mate40Pro','红色')
# iphome.record()
iphome.call(False)