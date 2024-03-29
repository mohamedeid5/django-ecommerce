from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name', )}
    
    list_display = (
        'id',
        'name',
        'slug'
    )
    
    list_display_links = ('name', )

admin.site.register(Category, CategoryAdmin)