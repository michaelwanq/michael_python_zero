data = [
    ["s001", "小明", 89],
    ["s002", "小张", 90],
    ["s003", "小找", 66],
]

import pandas as pd

df = pd.DataFrame(data,
    columns=["学号", "姓名", "成绩"])

df.to_excel("学生成绩excel文件.xlsx")
