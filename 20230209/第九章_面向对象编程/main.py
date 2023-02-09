"""
新建一个文件叫做动物animal.py
里面有一个类Animal
属性：name名字
方法：run奔跑
新建一个文件叫做羊sheep.py
里面有一个类Sheep，继承自animal
新增方法：eat_grass吃草，打印一句，我是羊在吃草
新建一个文件叫做老虎tiger.py
里面有一个类Tiger，继承自animal
新增方法：eat_meat吃肉，有个参数叫做animal，打印一句，我是老虎在吃{animal}
新建一个文件叫做main.py
引入sheep.py和tiger.py
初始化一个老虎、初始化一个羊
调用羊的eat_grass吃草，调用老虎的eat_meat吃肉方法把羊的对象作为参数传进去
"""
from sheep import Sheep
from tiger import Tiger
tiger1 = Tiger('hawk')
sheep1 = Sheep('michael')
sheep1.eat_grass()
tiger1.eat_meat(sheep1)