from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'website/index.html') 

def about(request):
    return HttpResponse('Hello, world. You are at chaiordjango About Page')

def contact(request):
    return HttpResponse('Hello, world. You are at chaiordjango Contact Page')