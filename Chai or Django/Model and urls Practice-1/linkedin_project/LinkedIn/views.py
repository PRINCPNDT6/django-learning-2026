from django.shortcuts import render
from .models import loginpage
from django.shortcuts import get_object_or_404
# Create your views here.
def Login_System(request):
    loginInfo = loginpage.objects.all()
    return render(request, 'LinkedIn/loginsystem.html', {
        'loginInformations': loginInfo
    })

def login_details(request, login_id):
    details = get_object_or_404(loginpage, pk = login_id)
    return render(request, 'LinkedIn/logindetails.html', {
        'detail': details
    } )

def book_Order(request, book_id):
    data = get_object_or_404(loginpage, pk = book_id)
    return render(request, 'LinkedIn/book.html', {
        'data': data
    })