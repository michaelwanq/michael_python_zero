"""
新建一个类叫做用户User
包含属性为用户名name和密码password
包含欢迎语welcome方法：你好name欢迎到来
新建子类Admin管理员
没有新属性
包含新方法，叫做管理系统，函数内输出“我在管理系统”
覆盖欢迎语welcome方法，输出：你好尊贵的Admin管理员name，欢迎归来
新建子类Vip贵宾用户
新属性为 money，充值金额
包含新方法，叫做提供贵宾服务vip_service，函数内输出“您好给你提供贵宾服务”
覆盖欢迎语welcome方法，输出：你好尊贵的VIP用户name，欢迎归来
初始化一个管理员Admin对象、两个Vip对象，两个普通用户，分别调用他们的方法
"""
class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def welcome(self):
        print(f"你好，{self.name}，欢迎到来！")

class Admin:
    def __init__(self):
        super().welcome()
