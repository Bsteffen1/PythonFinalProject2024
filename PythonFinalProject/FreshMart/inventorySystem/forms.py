# Form for an inventory item
#
# import Django forms and  then the models for Category and an Inventory item
from django import forms
from .models import Category, InventoryItem

#Sets the class of an InventoryItemForm which 
class InventoryItemForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
	class Meta:
		model = InventoryItem
		fields = ['name', 'quantity', 'category']