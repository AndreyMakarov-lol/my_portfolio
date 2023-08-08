from django.urls import path
from . import views
#Подключаем наш шаблон
urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>', views.AddComents.as_view(), name='add_comments')]
