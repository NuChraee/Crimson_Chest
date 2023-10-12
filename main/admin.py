from django.contrib import admin
from .models import *

@admin.register(Item)
class Product(admin.ModelAdmin):
    list_display = ('name', 'date_added', 'price', "sell", "amount", "modifiers")
    list_filter = ('date_added'),