from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def beth(request):
    return HttpResponse("Hello, beth. You're at the polls index.")

def yigit(request):
    return HttpResponse("Hello, yigit. You're at the polls index.")