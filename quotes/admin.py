from django.contrib import admin
from .models import Stock #so we have a model named stock in the models.py file so we are importing it here.

# Register your models here.
admin.site.register(Stock)