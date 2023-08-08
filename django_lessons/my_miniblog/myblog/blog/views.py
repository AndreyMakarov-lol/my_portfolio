from django.shortcuts import render, redirect
from django.views.generic.base import View

# Представление вывода записей

# Импортируем модель данных
from .models import Posts

class PostView(View):
    """Вывод записей"""
    def get(self, request):
        posts = Posts.objects.all()
        return render(request, 'blog/blog.html', {"post_list": posts})

class PostDetail(View):
    '''Отдельная страница для каждой записи'''
    def get(self, request, pk):
        post = Posts.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {"post": post})

class AddComents(View):
    """Добавление комментария"""
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")
