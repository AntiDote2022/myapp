from django.shortcuts import render



def index_page(request):
    return render(request, 'myapp1/index.html')


def about_page(request):
    return render(request, 'myapp1/about.html')


def account_login(request):
    return render(request, 'account/login.html')