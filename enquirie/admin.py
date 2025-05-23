from django.contrib import admin
from django.utils.html import format_html
from django.core.mail import send_mail
from django.urls import path
from django.shortcuts import redirect
from django.contrib import messages

from .models import enquiriesModel

class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'product_name', 'product_image', 'quantity', 'total_price', 'enquiry_date', 'is_verified', 'verify_button', 'remove_button']
    list_filter = ['enquiry_date', 'is_verified']
    readonly_fields = ['product_image', 'enquiry_date']
    date_hierarchy = 'enquiry_date'

    def product_name(self, obj):
        return obj.Product_id.pro_name if obj.Product_id else "-"
    product_name.short_description = 'Product Name'

    def product_image(self, obj):
        first_image = obj.Product_id.images.first() if obj.Product_id else None
        if first_image and first_image.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit: contain;" />', first_image.image.url)
        return "-"
    product_image.short_description = 'Product Image'

    def total_price(self, obj):
        if obj.Product_id and obj.quantity:
            return obj.Product_id.price * obj.quantity
        return "-"
    total_price.short_description = 'Total Price'

    def verify_button(self, obj):
        if not obj.is_verified:
            return format_html(
                '<a class="button" style="color: white; background: blue; padding: 6px 12px; border-radius: 4px;" href="{}">Verify</a>',
                f'verify/{obj.id}/'
            )
        return "Verified"
    verify_button.short_description = 'Verify Action'

    def remove_button(self, obj):
        return format_html(
            '<a class="button" style="color: white; background: #d9534f; padding: 6px 12px; border-radius: 4px;" onclick="return confirm(\'Are you sure you want to remove this enquiry?\')" href="{}">Remove</a>',
            f'remove/{obj.id}/'
        )
    remove_button.short_description = 'Remove Action'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('verify/<int:enquiry_id>/', self.admin_site.admin_view(self.verify_enquiry), name='verify-enquiry'),
            path('remove/<int:enquiry_id>/', self.admin_site.admin_view(self.remove_enquiry), name='remove-enquiry'),
        ]
        return custom_urls + urls

    def verify_enquiry(self, request, enquiry_id):
        enquiry = enquiriesModel.objects.get(id=enquiry_id)

        if enquiry.is_verified:
            messages.warning(request, "Already verified.")
        else:
            enquiry.is_verified = True
            enquiry.save()

            html_message = f"""
            <div style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 30px;">
                <div style="max-width: 600px; margin: auto; background: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
                    <div style="background-color: #102D59; padding: 20px; text-align: center;">
                        <h1 style="color: white;">VEERARAGAVAN FURNITURES</h1>
                        <h2 style="color: white;">Product Enquiry Verified</h2>
                    </div>
                    <div style="padding: 30px;">
                        <p style="font-size: 16px;">Dear <strong>{enquiry.name}</strong>,</p>
                        <p>Your enquiry for <strong>{enquiry.Product_id.pro_name}</strong> has been <span style="color: #4CAF50; font-weight: bold;">verified</span>.</p>
                        <p>We will contact you shortly with more details.</p>
                        <hr style="margin: 20px 0;" />
                        <p style="font-size: 14px; color: gray;">Thank you for choosing us!</p>
                    </div>
                </div>
            </div>
            """

            send_mail(
                subject='Your Product Enquiry Has Been Verified',
                message='Your enquiry has been verified.',
                from_email='samuelreegan372@example.com',
                recipient_list=[enquiry.email],
                fail_silently=False,
                html_message=html_message,
            )

            messages.success(request, f'Verified and email sent to {enquiry.email}')

        return redirect(request.META.get('HTTP_REFERER'))

    def remove_enquiry(self, request, enquiry_id):
        try:
            enquiry = enquiriesModel.objects.get(id=enquiry_id)
            enquiry.delete()
            messages.success(request, f"Enquiry from {enquiry.name} has been removed.")
        except enquiriesModel.DoesNotExist:
            messages.error(request, "Enquiry not found.")
        return redirect(request.META.get('HTTP_REFERER'))

admin.site.register(enquiriesModel, EnquiriesAdmin)
