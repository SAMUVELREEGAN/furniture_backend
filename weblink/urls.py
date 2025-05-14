from django.urls import path
from .views import WebLinkListView

urlpatterns = [
    path('', WebLinkListView.as_view(), name='weblink-list'),
]
