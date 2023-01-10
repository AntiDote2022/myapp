from django.shortcuts import render
from myapp1.models import Worker


def index_page(request):
    return render(request, 'myapp1/index.html')


def about_page(request):
    return render(request, 'myapp1/about.html')