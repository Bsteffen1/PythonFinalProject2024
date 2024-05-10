#Views which take a web request and returns a web response
#
#import of Django shortcuts, urls, and views/ import of the forms and models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from .forms import InventoryItemForm
from .models import InventoryItem, Category

#The defualt page template
class Index(TemplateView):
	template_name = 'inventorySystem/index.html'

#Dashboard class which request and grabs items from data base and returns it to the dashboard
class Dashboard(View):
	def get(self, request):
		items = InventoryItem.objects.order_by('id')
		return render(request, 'inventorySystem/dashboard.html', {'items': items})

#Adding items to the data base, gets the template and context of the category, adds the function to the button on dashboard
#Redirects back to dashboard when done
class AddItem(CreateView):
	model = InventoryItem
	form_class = InventoryItemForm
	template_name = 'inventorySystem/item_form.html'
	success_url = reverse_lazy('dashboard')
	#Gets the context of the category data
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context

#Edit item class that takes user back to the item form for the Item clicked
#Redirects back to dashboard when done
class EditItem(UpdateView):
	model = InventoryItem
	form_class = InventoryItemForm
	template_name = 'inventorySystem/item_form.html'
	success_url = reverse_lazy('dashboard')

#Takes user to the delete confimation page
#Redirects back to dashboard when done
class DeleteItem(DeleteView):
	model = InventoryItem
	template_name = 'inventorySystem/delete_item.html'
	success_url = reverse_lazy('dashboard')
	context_object_name = 'item'
