from django.contrib import admin

from demo.models import Adv
# from django.contrib.auth.models import User

# Register your models here.

@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'created_at', 'open']
    list_filter = ['user', 'open']

# @admin.register(User)
# class CommentUser(admin.ModelAdmin):
#     list_display = ['id', 'username']
#     list_filter = ['username',]