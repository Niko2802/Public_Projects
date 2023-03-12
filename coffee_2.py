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


# Замечания
# Убрать money из ингридиентов
# Из меню сделать словарь
# ing_drink = {} Заменить на словарь объектов класса Storage
# Вместо удаления элемента меню, сделать полное пересоздание меню и добавить это в __init__
# put_to_stor сделать через *args
# Сделать вывод в окно более правильным
# Выделить меню в отдельный класс


import PySimpleGUI as sg
import enum
drinks = {
    "kapuchino": {"milk": 200, "coffee": 15, "money": 100},
    "latte": {"milk": 250, "coffee": 7, "water": 50, "money": 150},
    "amerikano": {"water": 150, "coffee": 5, "money": 120},
    "latte with syrup": {"milk": 250, "coffee": 7, "water": 50, "syrup": 10, "money": 170},
    "coffee with cream": {"water": 150, "coffee": 10, "cream": 20, "money": 140}
}


class Ingridient(enum.Enum):
    milk = 1
    coffee = 2
    water = 3
    syrup = 4
    cream = 5
    # money = 6


class Recipe():
    def __init__(self, name, data, coast) -> None:
        self.name = name
        self.data = data
        self.coast = coast

    def name(self):
        return self.name

    def data(self):
        return self.data

    def coast(self):
        return self.coast


class Storage():
    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data
    
    def get_name(self):
        return self.name

    def get(self):
        return self.data

    def take(self, data):
        self.data -= data

    def put(self, data):
        self.data += data


class Menu():
    def __init__(self, storage) -> None:
        self.ing_drink = {}
        self.menu = {}
        # for name_drink in drinks:
        #     for ing in Ingridient:
        #         if ing.name in drinks.get(name_drink):
        #             self.ing_drink.update(
        #                 {ing.name: Storage(ing.name, drinks.get(name_drink)[ing.name])})
        #     self.menu.update({name_drink: Recipe(name_drink, self.ing_drink.copy(), drinks.get(name_drink)["money"])})
        #     self.ing_drink.clear()
        self.menu.clear()
        self.storage = storage
        self.ing_drink.clear()
        for name_drink in drinks:
            k = 0
            for ing in self.storage.values():
                if ing.data >= drinks.get(name_drink)[ing.name]:
                    k += 1
                    self.ing_drink.update(
                        {ing.name: Storage(ing.name, drinks.get(name_drink)[ing.name])})
            if k == len(drinks.get(name_drink))-1:
                self.menu.update({name_drink: Recipe(
                    name_drink, self.ing_drink.copy(), drinks.get(name_drink)["money"])})
            self.ing_drink.clear()

    def init_menu(self, storage):
        self.menu.clear()
        self.storage = storage
        self.ing_drink.clear()
        for name_drink in drinks:
            k = 0
            for ing in self.storage.values():
                if ing.data >= drinks.get(name_drink)[ing.name]:
                    k += 1
                    self.ing_drink.update(
                        {ing.name: Storage(ing.name, drinks.get(name_drink)[ing.name])})
            if k == len(drinks.get(name_drink))-1:
                self.menu.update({name_drink: Recipe(
                    name_drink, self.ing_drink, drinks.get(name_drink)["money"])})
            self.ing_drink.clear()
        return self.menu

    def list_menu(self):
        return self.menu.keys

    def get(self):
        return self.menu


class CoffeeMachine():
    def __init__(self) -> None:
        self.storage = {}
        self.money = 0
        # ing_drink = {}
        for ing in Ingridient:
            # if ing != Ingridient.money:
            self.storage.update({ing.name: Storage(ing.name, 500)})
            # else:
            #     self.storage.append(Storage(ing.name, 0))
        self.menu = Menu(self.storage)
    #     for name_drink in drinks:
    #         for ing in Ingridient:
    #             if ing.name in drinks.get(name_drink):
    #                 ing_drink.update(
    #                     {ing.name: Storage(ing.name, drinks.get(name_drink)[ing.name])})
    #         self.menu.update({name_drink: Recipe(name_drink, ing_drink.copy(), drinks.get(name_drink)["money"])})
    #         ing_drink.clear()

    # def list_menu(self):
    #     return self.menu

    # def list_names(self):
    #     return [x.name for x in self.menu]

    # def init_menu(self):
    #     old_menu = self.menu.copy()
    #     for item in old_menu:
    #         k = 0
    #         for stor in self.storage:
    #             if stor.name != Ingridient.money.name and item.data.get(stor.name, 0) > stor.data:
    #                 k += 1
    #         if k > 0:
    #             self.menu.remove(item)

    def cook(self, name):
        recipe = self.menu.get(name)
        for ing in recipe.data().values():
            self.storage.update({ing.get_name(): self.storage.get(ing.get_name()) - ing.get()})
        self.menu.init_menu()

    def put_to_stor(self, name, data):
        for stor in self.storage:
            if stor.name == name:
                stor.put(data)
        self.init_menu()


def create_layout():
    layout = []
    for item in coffee.list_menu():
        layout.append([sg.Button(button_text=item.name, size=(15, 1), key=item.name), sg.Text(
            text=f'{item.data[Ingridient.money.name]} рублей', size=(15, 1))])
    layout.append([sg.Text(text=f'Баланс машины {[x.data for x in coffee.storage if x.name == Ingridient.money.name][0]} рублей', key='balance'), sg.Button(
        button_text='Storage', key='storage')])
    return layout


coffee = CoffeeMachine()
layout = create_layout()
window = sg.Window('Кофе машина', layout)
menu = coffee.list_names().copy()
while True:
    event, values = window.read()
    if event in menu and event in coffee.list_names():
        coffee.cook(event)
        window['balance'].update(
            f'Баланс машины {[x.data for x in coffee.storage if x.name == Ingridient.money.name][0]} рублей')
        for r in menu:
            if r not in coffee.list_names():
                window[r].update(disabled=True)
    if event == 'storage':
        msg = ""
        for st in coffee.storage:
            if st.name != Ingridient.money.name:
                msg += (f'{st.name} {st.data} \n')
        sg.popup_ok(msg)
    if event in (None, 'Exit', 'Cancel'):
        break
