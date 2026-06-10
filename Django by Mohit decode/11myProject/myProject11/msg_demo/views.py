from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def show_msg(request):
    messages.debug(request, 'This is a debug Message')
    messages.info(request, 'THis is message info')
    messages.success(request, 'This is a success message')
    messages.warning(request, 'This is a warning message')
    messages.error(request, 'This is an error message')
    
    return render(request, 'msg_demo/show_msg.html')
