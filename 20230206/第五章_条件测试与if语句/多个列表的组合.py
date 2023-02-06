# 已注册的用户
curr_users = ["小明", "小王", "小李", "小董"]
# 新来的用户
new_users = ["小张", "小李", "小黑"]

for new_user in new_users:
    if new_user in curr_users:
        print("这用户已经被注册过了：", new_user)
    else:
        print("这个用户没被注册过：", new_user)
