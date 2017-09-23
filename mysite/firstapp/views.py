from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *
from .forms import *

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = suggestion_form(request.POST)
        if form.is_valid():
            modentry = suggestion(suggestion=form.cleaned_data['suggestion'])
            modentry.save()
    else:
        form = suggestion_form()
    suggestions = suggestion.objects.all()
    context = {"variable":suggestions, "form":form}
    return render(request,"default.html",context)

def page2(request):
    suggestions = suggestion.objects.all()
    toReturn = ""
    for sugg in suggestions:
        toReturn += sugg.suggestion + " "
    context = {"variable":toReturn}
    return render(request,"default.html",context)

def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
    else:
        form = registration_form()
    context = {"form":form}
    return render(request,"register.html",context)
