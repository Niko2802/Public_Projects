def calc_str(calc):
    operators = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    math_str = []
    stek = []
    num_temp = ""
    for s in calc:
        if s.isdigit():
            num_temp += s
        elif s == "," or s == ".":
            num_temp += s
        elif s in operators:
            if num_temp != "":
                math_str.append(float(num_temp))
                num_temp = ""
            if len(stek) == 0:
                stek.append(s)
            elif s == "(":
                stek.append(s)
            elif s == ")":
                while stek[-1] != "(":
                    math_str.append(stek.pop())
                stek.pop()
            elif operators.get(s) > operators.get(stek[-1]):
                stek.append(s)
            elif operators.get(s) <= operators.get(stek[-1]):
                for idx in range(len(stek)-1, -1, -1):
                    if operators.get(s) <= operators.get(stek[idx]) and stek[idx] != "(":
                        math_str.append(stek.pop())
                stek.append(s)
    math_str.append(float(num_temp))
    while stek != []:
        math_str.append(stek.pop())

    math_str.reverse()

    stek = []
    while math_str != []:
        tmp = math_str.pop()
        if tmp not in operators:
            stek.append(tmp)
        else:
            b = stek.pop()
            a = stek.pop()
            if tmp == "^":
                c = a ** b
            if tmp == "*":
                c = a * b
            if tmp == "/":
                c = a / b
            if tmp == "+":
                c = a + b
            if tmp == "-":
                c = a - b
            stek.append(c)
    return stek[0]


calc = input("Введите строку для расчёта: ")
calc = calc.replace(" ", "")

print(calc_str(calc))
