# Urls providing the web addresses for Inventory System
#
# Import Django admin and orginal urls, Then import views operations
from django.contrib import admin
from django.urls import path
from .views import Index, Dashboard, AddItem, EditItem, DeleteItem

# Paths to Index, Dashboard, Adding an item, Editing an item, and deleting an item
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
]
