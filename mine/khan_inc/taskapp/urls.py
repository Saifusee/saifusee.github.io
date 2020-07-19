from django.urls import path
from taskapp import views

appname = 'taskapp'
urlpatterns = [

   path("", views.index , name="list"),
   path("new", views.add, name="addnewtask")
]