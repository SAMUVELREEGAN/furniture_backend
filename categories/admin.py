from django.contrib import admin
from django.utils.html import format_html
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['image_tag' , 'categorie']
    search_fields = ['categorie']

    def image_tag(self, obj):
        if obj.pic:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 5px;" />', obj.pic.url)
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(Category, CategoryAdmin)
