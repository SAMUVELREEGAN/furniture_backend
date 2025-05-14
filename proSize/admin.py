from django.contrib import admin
from .models import ProductSize
from .forms import ProductSizeForm

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    form = ProductSizeForm
    list_display = ('category', 'sizes')
