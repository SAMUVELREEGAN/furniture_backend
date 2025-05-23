from django.contrib import admin
from django.utils.html import format_html
from .models import CarouselImage

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'created_at']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="60" style="object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Preview'

admin.site.register(CarouselImage, CarouselImageAdmin)
