from django.contrib import admin
from .models import Film, Actor
# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['film_id', 'title', 'description', 'release_year', 'language']
    list_filter = ['release_year']

# @admin.register(Actor)
# class ActorAdmin(admin.ModelAdmin):
#     list_display = ['actor_id', 'first_name', 'last_name']
#     list_filter = ['first_name']
