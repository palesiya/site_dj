from django.urls import path
from . import views
from home import  views as home
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home')),
    path('home/', home.home, name='home'),
    path('home/blog/', views.blog_news, name='bl_news'),
]
