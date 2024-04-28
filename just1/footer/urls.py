from django.urls import path
from footer.views import about_company

urlpatterns = [
    path('footer', about_company)
]