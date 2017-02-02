from django.http import HttpResponse
import datetime
from django.shortcuts import render
from addition.forms import Numbers


def hello(request):
    today = datetime.datetime.now().date()
    a = 10
    b = 19
    return render(request, "hello.html", {"today": a + b})


def addition(request):
    if request.method == "POST":
        form = Numbers(request.POST)
        add = int(form.data.get('number2')) + int(form.data.get('number1'))
        add_str = "Addition of two numbers is {}".format(add)
        return render(request, "addition.html", {"form": form, "addition": add_str})
    return render(request, "addition.html", {"form": Numbers()})
