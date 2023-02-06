def start_input():
    name = ""
    summa = ""
    accounts = {}
    for i in range(1, 6):
        acc = input(f"Введите номер счета {i}: ")
        if len(acc) == 6 and acc.isdigit():
            name = input(f"Введите имя владельца {i}: ")
            summa = input(f"Введите сумму на счете {i}: ")
            accounts[acc] = (name, summa)
        else:
            print("Введен не корректный номер счета!")
    return accounts


def put_cmd(accounts):
    if accounts == [] or len(accounts) < 2:
        acc = input("Введите номер счета на который хотите положить: ")
        bal = input("Введите сумму которую хотите положить: ")
        if len(acc) == 6 and acc in accounts:
            n, b = accounts[acc]
            b = float(b) + float(bal)
            accounts[acc] = (n, str(b))
        else:
            print("Введен не корректный счет.")
    elif accounts[0] in accounts:
        n, b = accounts[accounts[0]]
        b = float(b) + float(bal)
        accounts[accounts[0]] = (n, str(b))



def add_cmd(accounts):
    a = input(f"Введите номер счета: ")
    n = input(f"Введите имя владельца: ")
    s = input(f"Введите сумму на счете: ")
    if len(a) == 6 and a not in accounts:
        account = {a: (n, s)}
        accounts.update(account)
    else:
        print("Введенный счет уже существует или не равен 6 знакам")


def close_cmd(accounts):
    acc = input("Введите номер счет который хотите закрыть: ")
    val = accounts.pop(acc, None)
    if val == None:
        print("Введен не корректный счет.")


def take_cmd(accounts):
    acc = input("Введите номер счета с которого хотите взять: ")
    bal = input("Введите сумму которую хотите взять: ")
    if len(acc) == 6 and acc in accounts:
        n, b = accounts[acc]
        if float(b) >= float(bal):
            b = float(b) - float(bal)
            accounts[acc] = (n, str(b))
    else:
        print("Введен не корректный счет или сумма на счете меньше затребованной суммы")


def print_cmd(accounts):
    if accounts == {}:
        print("База пуста!")
    else:
        for i in accounts.items():
            a, b = i
            print(a, *b)


def tranf_cmd(accounts):
    acc_source = input("Введите номер счета с которого хотите перевести: ")
    acc_dest = input("Введите номер счета на который хотите перевести: ")
    bal = input("Введите сумму которую хотите перевести: ")
    if acc_source in accounts and acc_dest in accounts:
        n, b = accounts[acc_source]
        if float(b) >= float(bal):
            b = float(b) - float(bal)
            accounts[acc_source] = (n, str(b))
            n1, b1 = accounts[acc_dest]
            b1 = float(b1) + float(bal)
            accounts[acc_dest] = (n, str(b1))
    else:
        print("Проверьте введенные данные, операция не выполнена")


def exit_cmd(accounts):
    return None


cmd_map = {
    'put': put_cmd,
    'add': add_cmd,
    'close': close_cmd,
    'take': take_cmd,
    'print': print_cmd,
    'tranf': tranf_cmd,
    'exit': exit_cmd
}


print("Введите информацию о пяти счетах их владельцах и суммах на счетах")
accounts = start_input()

com = ""
while com.lower() != "exit":
    com = input("Введите команду (add, close, put, take, print, exit, tranf) следом можно ввести параметры команды (например: add счет ФИО сумма): ")
    l = com.split(" ")
    com = l.pop(0)
    cmd = cmd_map.get(com.lower())
    if cmd is None:
        print("Введенная команда не существует")
        continue
    cmd(l)

# Сделать загрузку базы из json при запуске программы и выгрузку при выходе. Сделать импорт, экспорт json по имени файла.
