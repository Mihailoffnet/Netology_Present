from django.shortcuts import render, HttpResponse
from .models import Film
# Create your views here.

def view_films(request):

    films_list = Film.objects.all()
    print(films_list.title)
    msg = films_list.title

    return HttpResponse(msg)