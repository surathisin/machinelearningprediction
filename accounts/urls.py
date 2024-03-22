# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('somepath/', views.some_view),
    # Define other app-specific paths
]
