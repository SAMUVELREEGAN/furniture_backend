# app/models.py
from django.db import models
from categories.models import Category

class ProductSize(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.CharField(max_length=100)  # Store sizes as comma-separated string

    def __str__(self):
        return f"{self.category.categorie} - {self.sizes}"
