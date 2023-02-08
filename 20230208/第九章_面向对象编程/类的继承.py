class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def info(self):
        print(f"车型是{self.model}，价格是{self.price}万元")


class OilCar(Car):
    def __init__(self, model, price, box_size):
        super().__init__(model, price)
        self.box_size = box_size

    def add_oil(self, money):
        print(f"老板，加{money}元的汽油")

    def info(self):
        super().info()
        print("我是油车，跑起来比电动车动力更足")


class ElectricCar(Car):
    def __init__(self, model, price, battery_size):
        super().__init__(model, price)
        self.battery_size = battery_size

    def add_electric(self, money):
        print(f"车值{self.price}元，充电花了{money}元")


ocar1 = OilCar("路虎", 60, 50)
ecar1 = ElectricCar('比亚迪', 30, 100)
print(ocar1.model, ocar1.price, ocar1.box_size)
ocar1.info()
ocar1.add_oil(500)
print(ecar1.model, ecar1.price, ecar1.battery_size)
ecar1.info()
ecar1.add_electric(200)
