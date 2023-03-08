from django.shortcuts import render


# Create your views here.
from webinterface.models import Item


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})

def about(request):
    return render(request, 'about.html', {})


def item_list(request):
   context = {
       'items': Item.objects.all()
   }
   return render(request, "Item_list.html", context)
