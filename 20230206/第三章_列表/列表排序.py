"""
列表打印使用方法list.sort()方法。
如果不想要改变原来的列表排序，可以使用方法sorted(list)方法
"""
# 方法一、分别打印列表排序
# grades = [77, 88, 73, 99, 82]
# print(f"grades列表如下：\n{grades}")
#
# grades.sort()
# print(f"使用sort方法进行排序：\n{grades}")
#
# grades.sort(reverse=True)
# print(f"使用sort方法进行降序排序：\n{grades}")
#
# grades = [77, 88, 73, 99, 82]
#
# new_grades = sorted(grades)
# print(f"使用sorted方法进行排序：\n{new_grades}")
#
# new_grades = sorted(grades, reverse=True)
# print(f"使用sorted方法进行降序排序：\n{new_grades}")
# print(f'当前grade列表顺序是：{grades}')
# 方法二、一次打印多个列表
grades = [77, 88, 73, 99, 82]
grades.sort()
sort_grade = grades
grades.sort(reverse=True)
reverse_sort = grades
print(f'使用sort方法排序结果是: {sort_grade}', f'使用sort(reverse=True)排序结果是:{reverse_sort}')

grades = [77, 88, 73, 99, 82]
sorted_grade = sorted(grades)
reverse_sorted = sorted(grades,reverse=True)
print(f'使用sort方法排序结果是: {sorted_grade}', f'使用sort(reverse=True)排序结果是:{reverse_sorted}')
print(f'排序完成后的grade列表是：{grades}')
