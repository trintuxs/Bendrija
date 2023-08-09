from django.shortcuts import render, get_object_or_404, redirect

from administracija.models import Kaupiamsis_Inasas
from darbuotojai.models import Darbuotojas
from gyventojas.models import Gyventojas, Butas


# Darbuotoju sarasas
def darbuotojai_list(request):
    darbuotojai = Darbuotojas.objects.all()
    return render(request, 'darbuotojai_list.html', {'darbuotojai': darbuotojai})


def darbuotojai_list(request):
    darbuotojai = Darbuotojas.objects.all()
    return render(request, 'darbuotojai_list.html', {'darbuotojai': darbuotojai})


def apmoketi(request):
    darbuotojai = Darbuotojas.objects.all()

    # Suskaičiuojame bendrą užmokesčio sumą
    total_wage = sum(darbuotojas.wage for darbuotojas in darbuotojai)

    # Gauname visų butų skaičių
    butai_count = Butas.objects.count()

    # Skaičiuojame užmokesčio dalį kiekvienam butui
    wage_per_butas = total_wage / butai_count

    # Apmokame kiekvieną buto savininką
    for butas in Butas.objects.all():
        butas.owner.apmoketi_darbuotojo_uzmokesti(wage_per_butas)

    return redirect('kaupiamasis_inasas')




