import win32net

users = win32net.NetUserEnum(None, 2, 0, 0)

print(users)

for user in users[0]:
    print(user['name'], user['num_logons'])