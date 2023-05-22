from django.urls import path
from hello import views
import hello.coffee_3 as c

storage = c.Storage.create(c.ingridients)
storage.fill(c.ingridients)
coffee = c.CoffeeMachine(storage, c.drinks, c.prices)


urlpatterns = [
    path("", views.menu),
    path("menu", views.menu),
    path("menu/<str:name>", views.buy),
    path("vault", views.vault)
    # path("about", views.about),
    # path("blog/<int:year>/", views.blogs),
    # path("test", views.test),
    # path("kapuchino", views.recipe, {"name": "kapuchino"}),
    # path("latte", views.recipe, {"name": "latte"}),
    # path("amerikano", views.recipe, {"name": "amerikano"}),
    # path("latte with syrup", views.recipe, {"name": "latte with syrup"}),
    # path("coffee with cream", views.recipe, {"name": "coffee with cream"})
    ]



# сделать несколько url-рецепт
# вывести сотав рецепта