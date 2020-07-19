from django.shortcuts import render
from django import forms
from django.urls import reverse

class NewTaskApp(forms.Form):
    task = forms.CharField(label="NEW TASK")
    priority=forms.IntegerField(label="Priority")

tasks = ["Running","Workout","Breakfast"]
# Create your views here.


def index(request):
    return render(request, "taskapp/index.html",{
        "tasks": tasks
    })
def add(request):
     return render(request, "taskapp/add.html",{
        "forms": NewTaskApp()
     })