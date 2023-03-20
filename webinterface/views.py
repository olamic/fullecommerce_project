from django.shortcuts import render


# Create your views here.
from webinterface.models import Item


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def item_list(request):
   context = {
       'items': Item.objects.all()
   }
   return render(request, "Item_list.html", context)
