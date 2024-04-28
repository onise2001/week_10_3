from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def odd_even(reques, num):
    
    if num % 2 == 0:
        return HttpResponse("This number is even")
    else:
        return HttpResponse("This number is odd")
