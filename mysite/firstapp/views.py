from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    form = suggestion_form()
    c_form = comment_form()
    suggestions = suggestion.objects.all().order_by('-authored')
    to_return = []
    for suggest in suggestions:
        data = {}
        data["suggestion"]=suggest.suggestion
        data["image"]=suggest.image
        data["idescription"]=suggest.idescription
        data["author"]=suggest.author
        data["comments"]=[]
        data["id"]=suggest.id
        comments = comment.objects.all().filter(suggestion=suggest).order_by('-authored')
        for comm in comments:
            data["comments"]+=[{"comment":comm.comment, "author":comm.author}]
        to_return+=[data]
    context = {"suggestions":to_return, "form":form, "comment_form":c_form}
    return render(request,"default.html",context)

@login_required
def suggestion_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = suggestion_form(request.POST, request.FILES)
            if form.is_valid():
                form.save(request)
                return redirect("/")
        else:
            form=suggestion_form()
    else:
        form = suggestion_form()
    context = {"form":form}
    return render(request,"suggest.html",context)

@login_required
def comment_view(request,suggest_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            c_form = comment_form(request.POST)
            if c_form.is_valid():
                suggest_instance = suggestion.objects.get(id=suggest_id)
                modentry = comment(
                    comment=c_form.cleaned_data['comment'],
                    author=request.user,
                    suggestion=suggest_instance
                    )
                modentry.save()
                return redirect("/")
        else:
            c_form = comment_form()
    else:
        c_form = comment_form()
    context = {"form":c_form, "suggestion":suggest_id}
    return render(request,"comment.html",context)

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
    suggestions = suggestion.objects.all().order_by('-authored')
    toReturn = {}
    toReturn["suggestions"]=[]
    for sugg in suggestions:
        toReturn["suggestions"]+=[{"suggest":sugg.suggestion}]
    return JsonResponse(toReturn)
