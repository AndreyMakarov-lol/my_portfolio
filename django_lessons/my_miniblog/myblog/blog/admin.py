from django.contrib import admin
from .models import Posts, Comments

# Регистрируем нашу мадель и настраиваем её отображение в админ панели

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
