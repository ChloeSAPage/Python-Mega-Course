from django.shortcuts import render
from django.views import generic
from .models import item

class MenuList(generic.ListView):
    pass
    #queryset = Item.object.


class MenuItemDetail(generic.DeleteView)