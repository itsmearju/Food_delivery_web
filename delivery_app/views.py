from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category, OrderModel

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        
        # get every item from each category
        appetizers = MenuItem.objects.filter(category_name_contains='Appetizer')
        entres = MenuItem.objects.filter(category_name_contains='Entre')
        desserts = MenuItem.objects.filter(category_name_contains='Dessert')
        drinks = MenuItem.objects.filter(category_name_contains='Drink')

        # pass into context
        context = { 'appetizers':appetizers, 'entres':entres, 'desserts':desserts, 'drinks':drinks }

        # render the template
        return render(request, 'customer/order.html', context)
