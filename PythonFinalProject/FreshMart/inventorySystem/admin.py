#Admin page
#Import django admin module and the models 
from django.contrib import admin
from .models import InventoryItem, Category

#Registers the Models to the admin page
admin.site.register(InventoryItem)
admin.site.register(Category)