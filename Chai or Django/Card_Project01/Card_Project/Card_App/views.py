from django.shortcuts import render
from .models import studentCards
from django.shortcuts import get_object_or_404
# Create your views here.
def All_Card(request):
    allcard = studentCards.objects.all()
    return render(request, 'Card_App/allCard.html', {
        'allcards': allcard
    })

def Card_Info(request, stu_id):
    stu_info = get_object_or_404(studentCards, pk = stu_id)
    return render(request, 'Card_App/cardsInfo.html', {
        'stuinfos': stu_info
    })
