def math_str_to_list(math_str):
    math_str = math_str.replace(" ", "")
    math_str_list = []
    n = ""
    z = ""
    for i in math_str:
        if i.isdigit():
            n += str(i)
            math_str_list.append(z)
            z = ""
        else:
            z += str(i)
            math_str_list.append(n)
            n = ""
    math_str_list.append(n)
    math_str_list = [x for x in math_str_list if x != ""]
    return math_str_list


def calculate(math_string, math_oper):
    iter = math_string.count(math_oper)
    for i in range(iter):
        idx = math_string.index(math_oper)
        a = math_string.pop(idx-1)
        b = math_string.pop(idx)
        if math_oper == "**":
            c = int(a) ** int(b)
        if math_oper == "*":
            c = int(a) * int(b)
        if math_oper == "/":
            c = int(a) / int(b)
        if math_oper == "+":
            c = int(a) + int(b)
        if math_oper == "-":
            c = int(a) - int(b)
        math_string.pop(idx-1)
        math_string.insert(idx-1, c)
    return math_string


operators = ['**', '*', '/', '+', '-']
calc = math_str_to_list(input("Введите строку для расчёта: "))
for i in operators:
    calculate(calc, i)
print("Результат вычислений: ", *calc)
# обратная польская запись
