from django.shortcuts import render, redirect


from darbuotojai.models import Staff
from gyventojas.models import  Flat


# Darbuotoju sarasas
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'darbuotojai_list.html', {'darbuotojai': staff})










