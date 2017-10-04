from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    form = suggestion_form()
    suggestions = suggestion.objects.all().order_by('-authored')
    context = {"variable":suggestions, "form":form}
    return render(request,"default.html",context)

def suggest(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = suggestion_form(request.POST)
            if form.is_valid():
                modentry = suggestion(
                    suggestion=form.cleaned_data['suggestion'],
                    author=request.user
                    )
                modentry.save()
        else:
            form=suggestion_form()
    else:
        form = suggestion_form()
    suggestions = suggestion.objects.all().order_by('-authored')
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

def suggestions(request):
    suggestions = suggestion.objects.all().order_by('authored')
    toReturn = {}
    toReturn["suggestions"]=[]
    for sugg in suggestions:
        toReturn["suggestions"]+=[{"suggest":sugg.suggestion}]
    return JsonResponse(toReturn)
