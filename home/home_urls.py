from django.urls import path
from blog.views import BlogView
from menu.views import MenuView
from home import views as home
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home')),
    path('home/', home.book_table, name='home'),
    path('home/blog/', BlogView.as_view(), name='bl_news'),
    path('home/menu/', MenuView.as_view(), name='menu'),
]
