from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import date
from utils import euclidean_dist
from utils.img import rectanglearea


def hello(request):
   welcome = "welcome again"

   text = """<h1>welcome to my app !</h1>"""
   html = welcome + text
   return HttpResponse(html)

def hello_render(request):
   # today = date.today()

   dist = euclidean_dist(0,0,2,2)

   area = rectanglearea(0,0,2,2)

   context = {'person':"Jhon Doe",
              'date': today,
              'distance':dist,
              'area': area}
   return render(request, "catalog/templates/hello.html", context)

def square(request, number):
   text = "square of number " + str(number) + " is " + str(number * number)
   return HttpResponse(text)
