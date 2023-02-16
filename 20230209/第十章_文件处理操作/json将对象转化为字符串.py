import json

data = [1, 2, 3, 4, 5]
print(json.dumps(data), type(json.dumps(data)))
data = {
    'xiaoming': [1, 2, 3, 4],
    'xiaozhang': [5, 6, 7, 8],
    'xiaozhao': [9, 10, 11, 12]
}
print(json.dumps(data), type(json.dumps(data)))
