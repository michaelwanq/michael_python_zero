# 怎样计算成绩的前三名：
# 新建一个列表grades，里面的值是[77, 88, 73, 99, 82, 89, 95, 86, 93]
# 将列表grades降序排序
# 输出成绩的最高分、最低分、平均分
# 提取grades的最高分前3名，打印结果
grades = [77, 88, 73, 99, 82, 89, 95, 86, 93]
max_grade = max(grades)
print('最高分是：',max_grade)
min_grade = min(grades)
print('最低分是：',min_grade)
sum_grade = sum(grades)
avarage_grade = sum_grade / len(grades)
print('平均分是：',avarage_grade)
# max_three_number = sorted(grades,reverse=True)[:3]
# print('这次考试的前三名成绩是：',max_three_number)
i = 1
for grade in sorted(grades,reverse=True)[:3]:
    print(f"第i名成绩是：{grade}")
    i += 1