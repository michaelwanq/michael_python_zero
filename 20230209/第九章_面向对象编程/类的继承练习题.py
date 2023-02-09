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
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def welcome(self):
        print(f"你好{self.name}欢迎到来")


class Admin(User):
    def __init__(self, name, password):
        super().__init__(name, password)

    def welcome(self):
        print(f"你好尊贵的Admin管理员{self.name}，欢迎归来")

    def manager(self):
        print("我在管理系统")


class VipUser(User):
    def __init__(self, name, password, money):
        super().__init__(name, password)
        self.money = money

    def welcome(self):
        print(f"你好尊贵的VIP用户{self.name}，欢迎归来")

    def vip_service(self):
        print("您好给你提供贵宾服务")

# 初始化一个管理员Admin对象、两个Vip对象，两个普通用户
admin01 = Admin("admin01", "1234")
admin02 = Admin("admin02", "1234")
vip01 = VipUser("vip01", "1234", 1000)
vip02 = VipUser("vip02", "1234", 2000)
user01 = User("user01", "1234")
user02 = User("user02", "1234")

admin01.welcome()
admin01.manager()
admin02.welcome()
admin02.manager()

vip01.welcome()
vip01.vip_service()
vip02.welcome()
vip02.vip_service()

user01.welcome()
user02.welcome()
"""
# 新建一个类叫做用户User
# 包含属性为用户名name和密码password
# 包含欢迎语welcome方法：你好name欢迎到来
# 新建子类Admin管理员
# 没有新属性
# 包含新方法，叫做管理系统，函数内输出“我在管理系统”
# 覆盖欢迎语welcome方法，输出：你好尊贵的Admin管理员name，欢迎归来
# 新建子类Vip贵宾用户
# 新属性为 money，充值金额
# 包含新方法，叫做提供贵宾服务vip_service，函数内输出“您好给你提供贵宾服务”
# 覆盖欢迎语welcome方法，输出：你好尊贵的VIP用户name，欢迎归来
# 初始化一个管理员Admin对象、两个Vip对象，两个普通用户，分别调用他们的方法

class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def welcome(self):
        print(f"你好，{self.name}，欢迎到来！")

class Admin(User):
    def __init__(self,name,password):
        super().__init__(name,password)
    def welcome(self):
        print(f'你好，尊贵的Admin管理员{self.name}，欢迎归来！')

    def manager(self):
        print('我在管理系统')

class Vip(User):
    def __init__(self,name,password,money):
        super().__init__(name,password)
        self.money = money

    def vip_service(self):
        print(f'您好,{self.name},给你提供贵宾服务!')

    def welcome(self):
        print(f'你好，尊贵的VIP用户{self.name}，欢迎归来！')

admin1 = Admin('a1','ap1')
admin1.welcome()
admin1.manager()
vip1 = Vip('v1','vp1',10)
vip2 = Vip('v2','vp2',20)
user1 = User('u1','123')
user2 = User('u2','234')
user1.welcome()
user2.welcome()
admin1.welcome()
admin1.manager()
vip1.welcome()
vip1.vip_service()
vip2.welcome()
vip2.vip_service()
"""
