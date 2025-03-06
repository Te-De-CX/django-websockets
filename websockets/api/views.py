from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def chat(request):
    return render(request,'chat.html')