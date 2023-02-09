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

# drinks = {
#     "kapuchino": {"milk": 200, "coffee": 15, "coast": 100},
#     "latte": {"milk": 250, "coffee": 7, "water": 50, "coast": 150},
#     "amerikano": {"water": 150, "coffee": 5, "coast": 120},
#     "latte_with_syrup": {"milk": 250, "coffee": 7, "water": 50, "syrup": 10, "coast": 170},
#     "coffee_with_cream": {"water": 150, "coffee": 10, "cream": 20, "coast": 140}
# }
import enum
import PySimpleGUI as sg


class Ingridient(enum.Enum):
    milk = 1
    coffee = 2
    water = 3
    syrup = 4
    cream = 5
    coast = 6


class Ingridients():
    def __init__(self) -> None:
        self.drinks = {
            "kapuchino": {"milk": 200, "coffee": 15, "coast": 100},
            "latte": {"milk": 250, "coffee": 7, "water": 50, "coast": 150},
            "amerikano": {"water": 150, "coffee": 5, "coast": 120},
            "latte with syrup": {"milk": 250, "coffee": 7, "water": 50, "syrup": 10, "coast": 170},
            "coffee with cream": {"water": 150, "coffee": 10, "cream": 20, "coast": 140}
        }

    def get(self, name=None):
        if name is None:
            return self.drinks
        else:
            return self.drinks[name]

    def add(self, drink):
        self.drinks.update(drink)


class Recipe():
    def __init__(self, name, data) -> None:
        self.name = name
        self.data = data


class StorageCapacity():
    def __init__(self) -> None:
        self.milk = 500
        self.water = 500
        self.coffee = 100
        self.cream = 100
        self.syrup = 100
        self.money = 0

    def get(self):
        return {"milk": self.milk, "water": self.water, "coffee": self.coffee, "cream": self.cream, "syrup": self.syrup, "money": self.money}

    def take(self, ingridients):
        self.milk -= ingridients.get("milk", 0)
        self.water -= ingridients.get("water", 0)
        self.coffee -= ingridients.get("coffee", 0)
        self.cream -= ingridients.get("cream", 0)
        self.syrup -= ingridients.get("syrup", 0)
        self.money += ingridients.get("coast")

    def put(self, ingridients):
        self.milk += ingridients.get("milk", 0)
        self.water += ingridients.get("water", 0)
        self.coffee += ingridients.get("coffee", 0)
        self.cream += ingridients.get("cream", 0)
        self.syrup += ingridients.get("syrup", 0)


class CoffeeMachine():
    def __init__(self) -> None:
        self.stor = StorageCapacity()
        self.ing = Ingridients()
        self.menu = []
        for item in self.ing.get():
            self.menu.append(Recipe(item, self.ing.get(item)))

    def list_menu(self):
        return self.menu

    def list_names(self):
        return [x.name for x in self.menu]

    def cook(self, name):
        self.stor.take(self.ing.get(name))
        old_menu = self.menu.copy()
        for item in old_menu:
            k = 0
            st = self.stor.get()
            for key in item.data:
                if key != "coast" and item.data[key] > st.get(key):
                    k += 1
            if k > 0:
                self.menu.remove(item)

    def add_to_stor(self, ingridients):
        self.stor.put(ingridients)

def create_layout():
    layout = []
    for item in coffee.list_menu():
        layout.append([sg.Button(button_text=item.name, size=(15, 1)), sg.Text(text=f'{item.data["coast"]} рублей', size=(15, 1))])
    return layout

coffee = CoffeeMachine()
layout = create_layout()
window = sg.Window('Кофе машина', layout)
while True: 
    event, values = window.read()
    if event is not None:
        coffee.cook(event)
        print(coffee.stor.get())
        print(coffee.list_names())
        for button in layout:
            if button[0].get_text() not in coffee.list_names():
                button[0].update(disabled=True)
    if event in (None, 'Exit', 'Cancel'):
        break
