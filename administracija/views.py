from django.db.models import Sum
from django.shortcuts import render
from gyventojas.models import Butas

# Create your views here.
def buto_inasai(request):
    flat_money = Butas.objects.annotate(inasu_suma=Sum('kaupiamsis_inasas__amount'))
    all_flats = Butas.objects.aggregate(visu_buto_suma=Sum('kaupiamsis_inasas__amount'))
    
    context = {
        'flat_money': flat_money,
        'all_flats': all_flats,
       
    }
    return render(request, 'buto_inasai.html', context=context)
