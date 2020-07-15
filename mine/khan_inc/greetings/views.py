from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greetall(request):
    return HttpResponse("Hii, There!!!....")


def inputnamegreet(request, inputname):
    return render(request, "greetings/greet.html",{
        "inputname":inputname.capitalize
    })