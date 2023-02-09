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
    money = 6


class Recipe():
    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data


class Storage():
    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data

    def get(self):
        return self.data

    def take(self, data):
        self.data -= data

    def put(self, data):
        self.data += data


class CoffeeMachine():
    def __init__(self) -> None:
        self.storage = []
        self.menu = []
        ing_drink = {}
        for ing in Ingridient:
            if ing.name != Ingridient.money.name:
                self.storage.append(Storage(ing.name, 500))
            else:
                self.storage.append(Storage(ing.name, 0))
        for name_drink in drinks:
            for ing in Ingridient:
                if ing.name in drinks.get(name_drink):
                    ing_drink.update(
                        {ing.name: drinks.get(name_drink)[ing.name]})
            self.menu.append(Recipe(name_drink, ing_drink.copy()))
            ing_drink.clear()

    def list_menu(self):
        return self.menu

    def list_names(self):
        return [x.name for x in self.menu]

    def cook(self, name):
        for rec in self.menu:
            if rec.name == name:
                for stor in self.storage:
                    if stor.name in rec.data and stor.name != Ingridient.money.name:
                        stor.take(rec.data[stor.name])
                    elif stor.name in rec.data and stor.name == Ingridient.money.name:
                        stor.put(rec.data[stor.name])
        old_menu = self.menu.copy()
        for item in old_menu:
            k = 0
            for stor in self.storage:
                if stor.name != Ingridient.money.name and item.data.get(stor.name, 0) > stor.data:
                    k += 1
            if k > 0:
                self.menu.remove(item)

    def put_to_stor(self, ingridients):
        self.stor.put(ingridients)


def create_layout():
    layout = []
    for item in coffee.list_menu():
        layout.append([sg.Button(button_text=item.name, size=(15, 1)), sg.Text(
            text=f'{item.data["money"]} рублей', size=(15, 1))])
    return layout


coffee = CoffeeMachine()
layout = create_layout()
window = sg.Window('Кофе машина', layout)
while True:
    event, values = window.read()
    if event is not None:
        coffee.cook(event)
        print([x.data for x in coffee.storage if x.name == "money"])
        print(coffee.list_names())
        for button in layout:
            if button[0].get_text() not in coffee.list_names():
                button[0].update(disabled=True)
    if event in (None, 'Exit', 'Cancel'):
        break
