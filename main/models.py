from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    sell = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    modifiers = models.TextField(null=True)
    amount = models.IntegerField(null=True)