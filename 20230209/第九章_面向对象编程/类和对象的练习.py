"""
新建一个类，叫做Phone手机
类中包含构造函数__init__
有两个形参model型号和price价格
在__init__中，将model和price，设置为self的变量
提供一个describe方法，描述手机的信息
返回“这是{model}手机，价格是{price}元”
提供另一个方法 call_friend(friend_name)，表示打电话给朋友
直接输出“我在用手机{self.model}打电话给{friend_name}”

初始化2个对象，一个是iphone13/6000元，另一个是华为p50/4000元
分别调用describe方法、并且调用打电话方法给你的朋友
"""


class Phone:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def describe(self):
        return f'这是{self.model}手机，价格是{self.price}元。'

    def call_friend(self, friend_name):
        print(f"我在用手机{self.model}打电话给{friend_name}。")


iphone13 = Phone('iphone13', 6000)
p50 = Phone('p50', 4000)
i_return = iphone13.describe()
print(i_return)
iphone13.call_friend("michael")
print('*' * 10)
p_return = p50.describe()
print(p_return)
p50.call_friend('hawk')
