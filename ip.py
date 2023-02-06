def is_ip(s):
    l = s.split(".")
    if len(l) != 4:
        return False
    for d in l:
        if not d.isdigit() or int(d) <= 0 or int(d) > 254:
            return False
    return True

ip = input("Введите строку: ")
print(ip.count(".") == 3 and all(d.isdigit() and int(d) >= 0 and int(d) <= 255 for d in ip.split(".")))

# print(is_ip(ip))
