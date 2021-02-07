# myapp/urls.py
from django.urls import path
# from .views import hello
# from .views import hello_render

from .views import *
urlpatterns = [
    path('', hello, name='homepage'),
    path('render_html', hello_render, name="hello_render"),
    path('square/<int:number>', square, name="square")
]