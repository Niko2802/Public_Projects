from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, {"name": "home"}),
    path("about", views.about),
    path("blog/<int:year>/", views.blogs),
    path("test", views.test)
    ]



# сделать несколько url-рецепт
# вывести сотав рецепта