from django.contrib import admin
from .models import Car, Person
# Register your models here

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['brand', 'model']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']
    list_filter = ['name', 'car']