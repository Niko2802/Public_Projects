# Пять компонентов кофе: кофе, вода, сливки, сироп, молоко.
# Рецепты с разным набором компонентов. Если ингридиентов не хватает, рецепт не доступен.
# У каждого рецепта своя цена.
# Реализовать структуру
# Сущности - кофемашина, рецепты, ингридиенты, емкость для хранения.

# Капучино - молоко - 200, кофе - 15
# Латте - молоко - 250, кофе - 7, вода - 50
# Американо - вода - 150, кофе - 5
# Латте с сиропом - молоко - 250, кофе - 7, вода - 50, сироп - 10
# Кофе со сливками - вода - 150, кофе - 10, сливки - 20


# 1. Много параметров при инициализации кофемашины
# 2. Нельзя пополнять после инициализации
# MVP - Model View Presenter 

import PySimpleGUI as sg

drinks = {
    "kapuchino": {"milk": 200, "coffee": 15},
    "latte": {"milk": 250, "coffee": 7, "water": 50},
    "amerikano": {"water": 150, "coffee": 5},
    "latte with syrup": {"milk": 250, "coffee": 7, "water": 50, "syrup": 10},
    "coffee with cream": {"water": 150, "coffee": 10, "cream": 20}
}

prices = {
    "kapuchino": 100,
    "latte": 150,
    "amerikano": 120,
    "latte with syrup": 170,
    "coffee with cream": 140
}

ingridients = {"milk": 1000, "coffee": 200,
               "water": 1000, "syrup": 20, "cream": 20}


class IngridientVault():
    def __init__(self, name, max_val) -> None:
        self.name = name
        self.max_val = max_val
        self.val = 0

    def add(self, val):
        self.val += val
        if self.val > self.max_val:
            self.val = self.max_val

    def take(self, val):
        self.val -= val
        if self.val < 0:
            self.val = 0

    def check(self, val):
        return self.val >= val


class Storage():
    def __init__(self) -> None:
        self.storage = {}

    @staticmethod
    def create(data):
        storage = Storage()
        for k, v in data.items():
            storage.config(IngridientVault(k, v))
        return storage

    def config(self, iv):
        self.storage[iv.name] = iv

    def add(self, name, val):
        iv = self.storage.get(name)
        if iv is not None:
            iv.add(val)

    def fill(self, data):
        for k, v in data.items():
            self.add(k, v)

    def cook(self, recipe):
        for k, v in recipe.items():
            iv = self.storage.get(k)
            if iv is not None:
                iv.take(v)

    def check(self, recipe):
        for k, v in recipe.items():
            iv = self.storage.get(k)
            if iv is None:
                return False
            if not iv.check(v):
                return False
        return True


class ConsoleMenu():
    def __init__(self, coffee) -> None:
        self.data = []
        self.coffee = coffee

    def init(self, lst):
        self.data.clear()
        for name, cost in lst:
            self.data.append(f"{name}: {cost}")
        self.data.append("exit")

    def select(self):
        for i, s in enumerate(self.data):
            print(f"{i+1}. {s}")
        s = input("Введите напиток:")
        return s
    
    def start(self):
        while True:
            lst = coffee.get_recipes()
            self.init(lst)
            res = self.select()
            if res == "exit":
                return
            self.coffee.cook(res)


class SimpleGUIMenu():
    def __init__(self, coffee) -> None:
        self.coffee = coffee
        self.window = sg.Window('Кофе машина', self.create_layout())
    
    def start(self):
        while True:
            name, values = self.window.read()
            if self.check(name):
                coffee.cook(name)
                self.window['balance'].update(
                    f'Баланс машины {[x.data for x in coffee.storage if x.name == Ingridient.money.name][0]} рублей')
                for r in menu:
                    if r not in coffee.list_names():
                        self.window[r].update(disabled=True)
            if name == 'storage':
                msg = ""
                for st in coffee.storage:
                    if st.name != Ingridient.money.name:
                        msg += (f'{st.name} {st.data} \n')
                sg.popup_ok(msg)
            if name in (None, 'Exit', 'Cancel'):
                break


    def create_layout(self):
        layout = []
        for k, v in coffee.get_recipes():
            layout.append([
                sg.Button(button_text=k, size=(15, 1), key=k), 
                sg.Text(text=f'{v} рублей', size=(15, 1))
            ])
        layout.append([
            sg.Text(text=f'Баланс машины {coffee.money} рублей', key='balance'), 
            sg.Button(button_text='Storage', key='storage')
            ])
        return layout




class CoffeeMachine():
    def __init__(self, storage, drinks, prices) -> None:
        self.drinks = drinks
        self.prices = prices
        self.money = 0
        self.storage = storage

    def cook(self, name):
        recipe = self.drinks.get(name)
        if recipe is not None:
            self.money += self.prices.get(name)
            print(self.money)
            self.storage.cook(recipe)

    def get_recipes(self):
        lst = []
        for k, recipe in self.drinks.items():
            if self.storage.check(recipe):
                lst.append((k, self.prices[k]))
        return lst


storage = Storage.create(ingridients)
storage.fill(ingridients)
coffee = CoffeeMachine(storage, drinks, prices)
menu = SimpleGUIMenu(coffee)
menu.start()
