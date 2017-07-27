from django.contrib import admin
from .models import Beer, Sale

# Register your models here.
admin.site.register(Beer)
admin.site.register(Sale)