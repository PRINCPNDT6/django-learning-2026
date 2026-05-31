from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.
def all_chai(request):
    Chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {
        'chais' : Chais
    })

def chai_details(request, chai_id):
    chai_detail = get_object_or_404(ChaiVarity, pk = chai_id)
    return render(request, 'chai/about.html', {
        'chai': chai_detail
    })
 
def OnePage(request):
    return render(request, 'chai/One.html')