from django.contrib import admin
from django.shortcuts import redirect
from .models import Craft

@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    # Disable "Add" if a Craft object already exists
    def has_add_permission(self, request):
        return not Craft.objects.exists()

    # Disable deletion
    def has_delete_permission(self, request, obj=None):
        return False

    # Redirect changelist to the edit page if object exists
    def changelist_view(self, request, extra_context=None):
        craft = Craft.objects.first()
        if craft:
            return redirect(f'/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/{craft.id}/change/')
        return super().changelist_view(request, extra_context)
