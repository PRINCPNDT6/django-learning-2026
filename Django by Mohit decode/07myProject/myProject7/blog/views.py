from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Form
# Create your views here.

def blog_list(request):
    blogs = [
        {"title": 'Django basic', 'is_feature': True, 'author': 'John Doe'},
        {"title": 'Django Advance', 'is_feature': True, 'author': 'Max'},
        {"title": 'Django Rest API', 'is_feature': False, 'author': 'Jarvis'},
    ]
    context = {
        'blogs': blogs, 
        'date': datetime.now(),
        'html_code': '<h1> Welcome to my Blog</h1>'
    }
    return render(request, 'blog/blog.html',context)

def home(request):

    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = Form.objects.create(
            username = username,
            password= password,
        )

        return redirect('profile', user.id)

    return render(request, 'home.html')

def about(request):
    return render(request, 'blog/about.html')

def profile(request, user_id):
    data = get_object_or_404(Form, id = user_id)

    return render(request, 'blog/profile.html', {
        'data':data
    })

def alluserData(request):
    alldata = Form.objects.all()
    return render(request, 'blog/alluserData.html',{
        'allData':alldata
    })

def editUser(request, user_id):
    user = get_object_or_404(Form, id = user_id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.password = request.POST.get("password")
    
        user.save()
        return redirect('alluserData')

    return render(request, 'blog/editUser.html')