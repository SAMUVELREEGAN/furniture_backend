from django.db import models
from product.models import *
import django.utils.timezone

# enquiries/models.py

class enquiriesModel(models.Model):
    quantity = models.IntegerField(null=True)
    name = models.TextField(max_length=200, null=True)
    phone_number = models.BigIntegerField(null=True, default=0)
    email = models.CharField(max_length=200, null=True)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='enquiries', null=True)
    enquiry_date = models.DateTimeField(auto_now_add=True)
    
    is_verified = models.BooleanField(default=False)  # <-- NEW

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

