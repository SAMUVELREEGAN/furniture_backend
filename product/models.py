from django.db import models
from categories.models import Category
from colorList.models import Color
from type.models import Type
from weblink.models import WebLink

class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.pro_name}"
    
class Product(models.Model):
    STAR_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    pro_name = models.CharField(max_length=255)
    description = models.TextField()
    star = models.CharField(max_length=3, choices=STAR_CHOICES, default='no')  # Dropdown
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, blank=True, null=True)
    link_name = models.ForeignKey(WebLink, on_delete=models.CASCADE)

    def __str__(self):
        return self.pro_name
