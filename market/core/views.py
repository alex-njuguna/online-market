from django.shortcuts import render
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "items": items
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
