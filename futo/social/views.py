from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'social/home.html')

def about(request):
    return render(request, 'social/about.html')

# Create your views here.
