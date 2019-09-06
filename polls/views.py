from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def base(request):
    return render(request, 'polls/base.html')


def login(request):
    return render(request, 'polls/login.html')
