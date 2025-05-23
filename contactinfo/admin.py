from django.contrib import admin
from django.shortcuts import redirect
from .models import Info

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    # Prevent showing the Add button if an Info object exists
    def has_add_permission(self, request):
        return not Info.objects.exists()

    # Prevent deleting the object
    def has_delete_permission(self, request, obj=None):
        return False

    # Redirect the changelist page directly to the edit page if Info exists
    def changelist_view(self, request, extra_context=None):
        info = Info.objects.first()
        if info:
            return redirect(f'/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/{info.id}/change/')
        return super().changelist_view(request, extra_context)
