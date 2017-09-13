from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"variable":"index page"}
    return render(request,"default.html",context)

def page2(request):
    context = {"variable":'page 2'}
    return render(request,"default.html",context)
