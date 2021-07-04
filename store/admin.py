from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name', )}
    
    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'category',
        'is_available',
        'created_date',
        'modified_date',
    )
    
    list_display_links = ('name', )

admin.site.register(Product, ProductAdmin)