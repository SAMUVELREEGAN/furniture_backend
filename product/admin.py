from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_name', 'price', 'category', 'color', 'type', 'star', 'link_name')
    search_fields = ['pro_name', 'category__categorie', 'color__color_name', 'type__type_name', 'link_name__link_name']
    list_filter = ['category', 'color', 'type', 'star', 'link_name']
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
