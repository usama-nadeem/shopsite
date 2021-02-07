from django.shortcuts import render
from django.http import HttpResponse

def order(request, quantity, item):
   text = "square of number " + str(number) + " is " + str(number * number)
   return HttpResponse(text)