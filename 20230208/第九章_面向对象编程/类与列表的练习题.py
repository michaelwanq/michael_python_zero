"""
婚礼接收彩礼程序
朋友结婚，你在门口帮忙收彩礼，需要记录来人的姓名和礼金

新建一个类叫Customer，访客的姓名name和礼金money
编写while True
输入”小明 1000”意思是小明给了1000的礼金，用这个数据构造对象
将对象放到customers这个列表里
如果输入quit就退出，退出之前遍历列表，计算打印信息：
访客总人数、访客礼金总金额、最大金额、最小金额、平均金额
"""
class Customer:
    def __init__(self,name,money):
        self.name = name
        self.money = money

customers = []
while True:
    print("#" * 20)
    info = input("请输入来人姓名和金额：")
    if info == "quit":
        break
    # 将input获取的客户输入使用split进行分割
    name, money = info.split()
    # 注意input得到的用户输入都是字符串，需要进行类型转换
    money = int(money)
    # 使用Customer类创建实例
    customer = Customer(name, money)
    # 将创建的对象放到列表customers中
    customers.append(customer)
print(customers)
print("访客总人数:", len(customers))
# 将列表中实例的属性赋值给变量money
moneys = [c.money for c in customers]
print("总金额:", sum(moneys))
print("最大金额:", max(moneys))
print("最小金额:", min(moneys))
print("平均金额:", sum(moneys) / len(moneys))