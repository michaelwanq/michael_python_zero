"""
朋友排排队：
新建一个空列表heights，代表你的朋友的身高
给这个列表heights，依次append添加5个值，例如178.4、179.3、176.8、180.5、177.7
统计长度输出文本，例如“列表中有5个值”
将列表按降序排列，输出列表的结果
"""
heights = []
friend_height = [178.4, 179.3, 176.8, 180.5, 177.7]
for height in friend_height:
    heights.append(height)
    print(f'当前heights列表为：{heights}')

print(f'输入完成，heights列表包含元素个数为：{len(heights)}')
reverse_heights = sorted(heights,reverse=True)
print(f'heights列表降序排列结果为：{reverse_heights}')
print(f'heights列表顺序为：{heights}')
