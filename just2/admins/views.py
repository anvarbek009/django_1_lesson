from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def admin_page(request):
    return HttpResponse("Hello, this is admin")

def user_page(request):
    return HttpResponse("Hello, this page for users.")