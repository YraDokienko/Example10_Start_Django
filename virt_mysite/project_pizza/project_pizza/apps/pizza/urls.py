from django.urls import path
from .views import base_view

urlpatterns = [
    path(r'', base_view),
]