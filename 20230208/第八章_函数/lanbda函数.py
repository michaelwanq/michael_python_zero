sgrades = [("xiaoming", 89), ("xiaozhao", 77), ("xiaoxiaozhang", 99)]
sgrades.sort()
print(sgrades)

print('*' * 10)
sgrades = [("xiaoming", 89), ("xiaozhao", 77), ("xiaoxiaozhang", 99)]
sgrades.sort(key=lambda x: x[1])
print(sgrades)

print('*' * 10)
sgrades = [("xiaoming", 89), ("xiaozhao", 77), ("xiaoxiaozhang", 99)]
new_list = sorted(sgrades, key=lambda x: x[1], reverse=True)
print(new_list)
