from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            Contact.objects.create(name = name, message = message)
            return redirect('submit_contact')
        else:
            return redirect('contact_form')
    return render(request, 'contact/contact_form.html')


def submit_contact(request): 
    # formData = Contact.objects.all()
    formData = Contact.objects.last()
    return render(request, 'contact/submit_contact.html', {
        'formData': formData

    })