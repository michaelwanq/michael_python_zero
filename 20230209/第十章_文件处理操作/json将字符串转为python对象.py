import json

# 特别注意：此处需要用双引号处理，单引号会导致报错
data_string = """
{"xiaoming": [1, 2, 3, 4],"xiaozhang": [5, 6, 7, 8],"xiaozhao": [9, 10, 11, 12]}
"""

data = json.loads(data_string)
print(type(data))
print(data)
