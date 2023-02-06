"""
定义一个字典：
初始化3个人的信息，key是朋友的名字，value是他喜欢的水果
例如：xiaoming:apple
添加2个人的 键值对，即新的名字:喜欢的水果数据对
根据人名，更新一个人喜欢的水果，例如从orange改成apple
打印最新的结果数据
"""
fruits = {"小张": 'apple',
'小李': 'orange',
'小赵': 'banana'
}
fruits['小钱'] = 'peer'
fruits['小万'] = 'grape'
print(fruits)

fruits['小万'] = 'mango'
print(fruits)
