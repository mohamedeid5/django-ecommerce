from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name          = models.CharField(max_length=200)
    slug          = models.SlugField(max_length=400)
    description   = models.TextField(max_length=500, blank=True)
    price         = models.IntegerField()
    image         = models.ImageField(upload_to='images/products')
    stock         = models.IntegerField()
    is_available  = models.BooleanField(default=True)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date  = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detial', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.name