from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ( 'image_tag','pro_name', 'price', 'category', 'color', 'type', 'star', 'link_name')
    search_fields = ['pro_name', 'category__categorie', 'color__color_name', 'type__type_name', 'link_name__link_name']
    list_filter = ['category', 'color', 'type', 'star', 'link_name']
    inlines = [ProductImageInline]

    def image_tag(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 5px;" />', first_image.image.url)
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(Product, ProductAdmin)
