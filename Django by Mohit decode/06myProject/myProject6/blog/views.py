from django.shortcuts import render

# Create your views here.
from datetime import datetime

def blog_details(request):
    post = {
        'title': 'my second templtes page ',
        'description': 'Django is a high level language',
        'author': None,
        'created_at': datetime(2025, 8, 19, 10, 30),
        "comments_count": 5,
        'tags': ["Django", "Pyhton", "web development"],
        "price": 1000,
        'rollnumber':317,
    }
    
    return render(request, 'blog/blog_details.html', {
        'post':post
    })