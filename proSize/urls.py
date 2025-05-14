from django.urls import path
from .views import ProductSizeListView

urlpatterns = [
    path('', ProductSizeListView.as_view(), name='product-size-list'),
]
