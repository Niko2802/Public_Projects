from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

drinks = {
    "kapuchino": {"milk": 200, "coffee": 15},
    "latte": {"milk": 250, "coffee": 7, "water": 50},
    "amerikano": {"water": 150, "coffee": 5},
    "latte with syrup": {"milk": 250, "coffee": 7, "water": 50, "syrup": 10},
    "coffee with cream": {"water": 150, "coffee": 10, "cream": 20}
}


# def home(request, name):
#     return HttpResponse(f"Hello django {name}")

# def about(request):
#     print(request.body)
#     print(request.method)
#     print(request.GET)
#     print(request.COOKIES)
#     return HttpResponse("Info about me")

# def blogs(request, year):
#     return HttpResponse(f"<h2>blog {year}</h2>")

# def test(request):
#     return HttpResponseRedirect("about")

# def recipe(request, name):
#     rec = drinks.get(name)
#     ing = rec.keys()
#     ing_str = ""
#     for i in ing:
#         ing_str += i + " " + str(rec.get(i)) + "<br>"
#     page = f"<h2>Рецепт кофе {name}</h2><br>{ing_str}"
#     return HttpResponse(page)

def menu(request, coffee):
    # context = {
    #     "drinks": {
    # "kapuchino": "Капучино",
    # "latte": "Латте",
    # "amerikano": "Американо",
    # "latte with syrup": "Латте с сиропом",
    # "coffee with cream": "Кофе со сливками",
    # "raf": "Раф"}
    # }
    drin = {}
    drin.update(x for x in coffee.get_recipes())
    print(drin)
    context = {"drinks": drin}
    return render(request, "menu.html", context=context)

def vault(request):
    pass

def buy(request, name, coffee):
    context = {}
    return render(request, "ingridients.html", context=context)




# Все элементы span нужно сделать жирными
# Фон страницы сделать кофейного цвета
# ! Сделать фон на всю страницу
# Подключить код кофемашины к проекту Django
# Сделать страницу Vault
# Реализовать Post запрос на кнопку купить
# 
# 
# 
