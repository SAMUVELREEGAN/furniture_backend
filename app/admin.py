from django.contrib import admin
from django.utils.html import format_html
from .models import AboutModel, ContactUsModel, ContactSettingModel


class AboutModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'about_story_img_preview',
        'card_1_img_preview',
        'card_2_img_preview',
        'card_3_img_preview',
        'card_4_img_preview',
        'designer_img_preview',
    ]
    readonly_fields = list_display[1:]

    def image_preview(self, image_field):
        if image_field:
            return format_html(
                '<img src="{}" width="100" height="50" style="object-fit:cover" />', image_field.url
            )
        return "(No Image)"

    def about_story_img_preview(self, obj):
        return self.image_preview(obj.about_story_img)

    def card_1_img_preview(self, obj):
        return self.image_preview(obj.card_1_img)

    def card_2_img_preview(self, obj):
        return self.image_preview(obj.card_2_img)

    def card_3_img_preview(self, obj):
        return self.image_preview(obj.card_3_img)

    def card_4_img_preview(self, obj):
        return self.image_preview(obj.card_4_img)

    def designer_img_preview(self, obj):
        return self.image_preview(obj.designer_img)

    about_story_img_preview.short_description = "About Story Image"
    card_1_img_preview.short_description = "Card 1 Image"
    card_2_img_preview.short_description = "Card 2 Image"
    card_3_img_preview.short_description = "Card 3 Image"
    card_4_img_preview.short_description = "Card 4 Image"
    designer_img_preview.short_description = "Designer Image"

admin.site.register(AboutModel, AboutModelAdmin)


class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'ph_number', 'subject', 'message', 'created_at']
    search_fields = ['name', 'email', 'subject']

admin.site.register(ContactUsModel, ContactUsModelAdmin)


class ContactSettingModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact_top_img_tag', 'contact_bottom_img_tag']

    def contact_top_img_tag(self, obj):
        if obj.contact_top_img:
            return format_html('<img src="{}" width="50" height="50" />', obj.contact_top_img.url)
        return "-"
    contact_top_img_tag.short_description = 'Top Image'

    def contact_bottom_img_tag(self, obj):
        if obj.contact_bottom_img:
            return format_html('<img src="{}" width="50" height="50" />', obj.contact_bottom_img.url)
        return "-"
    contact_bottom_img_tag.short_description = 'Bottom Image'

admin.site.register(ContactSettingModel, ContactSettingModelAdmin)