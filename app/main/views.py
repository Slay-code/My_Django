from django.shortcuts import render

from .models import Services


def index(request):
    context = {
        'title': 'Простой сайт',
        'H': 'Добро пожаловать на мой сайт!',
        'services': Services.objects.all()
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'H': 'О нашей компании',
    }
    
    return render(request, 'main/about.html', context)


def service(request):
    context = {
        'title': 'Услуги',
        'H': 'Услуги нашей компании',
        'services': Services.objects.all()
    }
    
    return render(request, 'main/service.html', context)
