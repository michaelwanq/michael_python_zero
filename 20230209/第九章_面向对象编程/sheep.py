from animal import Animal
class Sheep(Animal):
    def __init__(self,name):
        super().__init__(name)

    def eat_grass(self):
        print(f"我是sheep_{self.name},正在吃草。")