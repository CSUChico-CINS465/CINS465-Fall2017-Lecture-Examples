from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from .forms import *

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
