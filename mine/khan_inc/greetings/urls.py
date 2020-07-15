from django.urls import path
from . import views

urlpatterns = [

    path("", views.greetall, name="greetall"),
    path("<str:inputname>", views.inputnamegreet,name="inputname")
]