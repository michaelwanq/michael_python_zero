print("*" * 10)
value = "apple"

print(value == "banana")
print(value == "apple")
print(value == "pear")

print("*" * 10)
value = "apple"

print(value != "banana")
print(value != "apple")
print(value != "pear")

print("*" * 10)
a, b = 3, 7

print("a == b", a == b)
print("a != b", a != b)
print("a > b", a > b)
print("a >= b", a >= b)
print("a < b", a < b)
print("a <= b", a <= b)

print("*" * 10)
numbers = [1, 3, 5, 7, 9]
print("3 in numbers: ", 3 in numbers)
print("3 not in numbers: ", 3 not in numbers)

print("*" * 10)
fruits = ["apple", "pear", "orange"]
print("banana in fruits: ", "banana" in fruits)
print("banana not in fruits: ", "banana" not in fruits)

print("*" * 10)
print(a == 3 and "pear" not in fruits)
print(a == 3 and "pear" not in fruits and value == "ok")
print(a == 3 and ("pear" not in fruits) and value == "ok")

print("*" * 10)
print(a == 3 or "pear" not in fruits)
print(a == 3 or "pear" not in fruits or value == "ok")
print(a == 3 or ("pear" not in fruits) or value == "ok")
print(a == 3 and "pear" not in fruits or value == "ok")
print(a == 3 or "pear" not in fruits and value == "ok")
print((a == 3 or "pear" not in fruits) and value == "ok")
