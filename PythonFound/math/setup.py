from distutils.core import setup

setup(
    name="baizhanSuperMath",#对外模块的名称
    version='2.0',#版本号
    description="对外发布的模块，里面只有数学方法",#描述
    author="jilong",#作者
    author_email="jilong930323@163.com",
    py_modules=["baizhanSuperMath.demo1","baizhanSuperMath.demo2"]#要发布的模块
)