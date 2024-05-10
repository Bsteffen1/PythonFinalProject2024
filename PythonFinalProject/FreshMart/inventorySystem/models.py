#Models of Invetory Item and Category
#
#import of the models from django database module
from django.db import models

#Inventory item django model with the name, quantity, and category
class InventoryItem(models.Model):
	name = models.CharField(max_length=200)
	quantity = models.IntegerField()
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	#Overrides str method to show the name of the model item
	def __str__(self):
		return self.name

#Model for the category field, the name of the category
class Category(models.Model):
	name = models.CharField(max_length=200)

	#Fixes the admin panel plural name
	class Meta:
		verbose_name_plural = 'categories'
	#Overrides str method to show the name of the model item
	def __str__(self):
		return self.name