"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app.views import home_view, time_view, workdir_view,\
    hello_view, hello_name, sum_view, pagi_view, create_car, \
    list_car, create_person, list_person


urlpatterns = [
    path('', home_view, name='home'),
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('hello/', hello_view, name='hello'),
    path('hello_name/', hello_name, name='hello_name'),
    path('pagi/', pagi_view, name='pagi'),
    path('sum/<int:a>/<int:b>/', sum_view, name='sum'),
    path('newcar/', create_car, name='newcar'),
    path('cars/', list_car, name='cars'),
    path('newperson/', create_person, name='newperson'),
    path('people/', list_person, name='people'),
    path('admin/', admin.site.urls, name='admin'),
]