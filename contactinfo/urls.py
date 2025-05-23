# contactinfo/urls.py
from django.urls import path
from .views import InfoCreateView, InfoListView

urlpatterns = [
    path('create/', InfoCreateView.as_view(), name='info-create'),  # POST
    path('list/', InfoListView.as_view(), name='info-list'),        # GET
]
