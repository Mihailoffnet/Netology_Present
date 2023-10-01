from django.contrib import admin
from demo.models import Comment
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'created_at']
    list_filter = ['user',]

# @admin.register(User)
class CommentUser(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_filter = ['username',]