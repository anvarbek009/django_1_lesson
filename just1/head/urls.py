from django.urls import path
from .views import get_lokation

urlpatterns = [
    path('lokation', get_lokation)
]