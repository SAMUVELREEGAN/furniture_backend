from django.urls import path
from .views import *

urlpatterns = [
    path('', Craft.as_view(), name='Craft-size-list'),
]
