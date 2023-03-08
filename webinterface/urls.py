from django.urls import path
from . import views
from .views import item_list

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('item', item_list, name='item_list'),
    path('about', views.about, name='about'),
]
