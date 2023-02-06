numbers = list(range(10))
print(numbers)
# 从2位置开始，到位置5结束，不包含位置5
print("2:5", numbers[2:5])
# 从0开始，到6位置结束，不包含6
print(":6", numbers[:6])
# 从3开始，到结束
print("3:", numbers[3:])
# 包含所有的元素
print(":", numbers[:])
# 从3开始，到9，步长为2
print("3:9:2", numbers[3:9:2])
