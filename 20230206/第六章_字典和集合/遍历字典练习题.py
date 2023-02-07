"""
小明 apple
小花 orange
小张 banana
小白 pear
朋友 小明 最喜欢的水果是 apple
朋友 小花 最喜欢的水果是 orange
朋友 小张 最喜欢的水果是 banana
朋友 小白 最喜欢的水果是 pear
"""
fruits = {
    '小明': 'apple',
    '小花': 'orange',
    '小张': 'banana',
    '小白': 'pear'
}
for k,v in fruits.items():
    print(f"朋友 {k} 最喜欢的水果是 {v}。")