from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin_page),
    path('user/', user_page)
]