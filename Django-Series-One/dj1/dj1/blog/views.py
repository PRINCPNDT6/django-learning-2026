from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def home(request):
    context = {
        'name': "Prince",
        "age": 20,
        'skill': ["Python", 'Django', 'React'],
        'user': User('kumar', 30),
        'blog': {
            'title': 'Django Template',
            'Content': '<b>This is Bold</b>',
            'created_at': datetime(2025, 8, 18, 10, 30)
        },
        'empty_value': None
    }
    return render(request,'blog/blog.html', context)