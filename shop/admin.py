from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Admin panelda nimalar ko'rinishi:
    list_display = ('name', 'price', 'is_bestseller', 'is_new')
    list_editable = ('price', 'is_bestseller', 'is_new')
    search_fields = ('name', 'description') # Endi tavsif bo'yicha ham qidira olasan