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

drinks = {
    "kapuchino": {"milk": 200, "coffee": 15, "coast": 100},
    "latte": {"milk": 250, "coffe": 7, "water": 50, "coast": 150},
    "amerikano": {"water": 150, "coffee": 5, "coast": 120},
    "latte_with_syrup": {"milk": 250, "coffee": 7, "water": 50, "syrup": 10, "coast": 170},
    "coffee_with_cream": {"water": 150, "coffee": 10, "cream": 20, "coast": 140}
}


class Recipe():
    def __init__(self, name) -> None:
        self.name = name
        self.data = drinks.get(name)


class StorageCapacity():
    def __init__(self) -> None:
        self.milk = 500
        self.water = 500
        self.coffee = 100
        self.cream = 100
        self.syrup = 100
        self.money = 0

    def get(self):
        return {"milk": self.milk, "water": self.water, "coffee": self.coffee, "cream": self.cream, "syrup": self.syrup}

    def take(self, ingridients):
        self.milk -= ingridients.get("milk", 0)
        self.water -= ingridients.get("water", 0)
        self.coffee -= ingridients.get("coffee", 0)
        self.cream -= ingridients.get("cream", 0)
        self.syrup -= ingridients.get("syrup", 0)

    def put(self, ingridients):
        self.milk += ingridients.get("milk", 0)
        self.water += ingridients.get("water", 0)
        self.coffee += ingridients.get("coffee", 0)
        self.cream += ingridients.get("cream", 0)
        self.syrup += ingridients.get("syrup", 0)

    def money(self, money):
        pass


class CoffeeMachine():
    def __init__(self) -> None:
        pass


recipe = Recipe("latte")
stor = StorageCapacity()
stor.get({"milk": 100})
