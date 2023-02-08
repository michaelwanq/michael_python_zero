"""
编写第1个函数：compute(x,y,method)
如果method==add字符串，返回x+y
如果method==sub字符串，返回x-y
如果method==mul字符串，返回x*y
如果method==div字符串，返回x/y

编写第2个函数：add(x, y)调用compute(x,y,method=add)得到结果返回
编写第3个函数：sub(x, y)调用compute(x,y,method=sub)得到结果返回

填写参数调用add和sub函数，输出结果
"""
import compute

print(compute.add(9, 6))
print(compute.sub(9, 6))
