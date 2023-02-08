def compute(x, y, method):
    if method == 'add':
        return x + y
    elif method == 'sub':
        return x - y
    elif method == 'mul':
        return x * y
    elif method == 'div':
        return x / y


def add(x, y):
    # add_result = compute(x, y, method='add')
    # print(add_result)
    # return add_result
    return compute(x,y,method='add')

def sub(x, y):
    # sub_result = compute(x, y, method='sub')
    # print(sub_result)
    # return sub_result
    return compute(x,y,method='sub')