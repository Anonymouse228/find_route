from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'name': 'Bob',
    }
    return render(request, 'home.html', context)
