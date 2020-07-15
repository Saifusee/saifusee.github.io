from django.urls import path
from . import views

urlpatterns = [

    path("", views.greetall, name="greet_tall"),
    path("github_html", views.git, name="git_file"),
    path("<str:inputname>", views.inputnamegreet,name="inputname")
    
]