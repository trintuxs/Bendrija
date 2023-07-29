from django.shortcuts import render

from gyventojas.models import Gyventojas, Butas


# Create your views here.
def index(request):
    rezident = Gyventojas.objects.count()
    flats = Butas.objects.count()
    context = {
        'rezident': rezident,
        'flats': flats
    }
    return render(request, 'index.html', context=context)


