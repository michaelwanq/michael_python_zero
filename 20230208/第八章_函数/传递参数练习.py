"""
编写如下函数
函数名字，叫做compute,意思是计算
参数分别是x、y、method，代表数字x、数字y、字符串method
如果method==add字符串，打印x+y
如果method==sub字符串，打印x-y
如果method==mul字符串，打印x*y
如果method==div字符串，打印x/y
method设置成带默认值的参数，默认为默认加法
分别用如下方式调用函数
位置参数
关键字参数，可以换顺序
带默认值参数和和不带默认值参数调用
"""


def compute(x, y, method='add'):
    if method == 'add':
        add_values = x + y
        print(f'{x} + {y} = ', add_values)
    elif method == 'sub':
        sub_values = x - y
        print(f'{x} - {y} = ', sub_values)
    elif method == 'mul':
        mul_values = x * y
        print(f'{x} * {y} = ', mul_values)
    elif method == 'div':
        div_values = int(x / y)
        print(f'{x} / {y} = ', div_values)


compute(5, 3, 'sub')
compute(5, 3, 'mul')
compute(10, 2, 'div')
compute(y=6, x=9, method='sub')
compute(x=9, y=3, method='div')
compute(x=2, y=4)
