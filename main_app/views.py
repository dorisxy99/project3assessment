from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import WishItem

# Create your views here.
class WishList(ListView):
    model = WishItem

class WishCreate(CreateView):
    model = WishItem
    fields = ['item']
    success_url = '/'

class WishDelete(DeleteView):
    model = WishItem
    success_url = '/'