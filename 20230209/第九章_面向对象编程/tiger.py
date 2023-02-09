from animal import Animal
class Tiger(Animal):
    def __init__(self,name):
        super().__init__(name)

    def eat_meat(self,eat_animal):
        # e_animal = animal
        print(f'我是tiger_{self.name},在吃{eat_animal.name}!')
