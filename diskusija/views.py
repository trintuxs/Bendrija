from django.shortcuts import render, get_object_or_404, redirect

from gyventojas.models import Gyventojas
from .models import Diskusija, Komentaras
from django.contrib.auth.decorators import login_required

def diskusija_perziureti(request, diskusijos_id):
    diskusija = get_object_or_404(Diskusija, id=diskusijos_id)
    komentarai = Komentaras.objects.filter(diskusija=diskusija)
    context = {'diskusija': diskusija, 'komentarai': komentarai}
    return render(request, 'diskusija_perziureti.html', context = context)

@login_required
def prideti_komentara(request, diskusijos_id):
    diskusija = get_object_or_404(Diskusija, id=diskusijos_id)
    if request.method == 'POST':
        turinys = request.POST['turinys']
        gyventojas = Gyventojas.objects.get(user=request.user)
        Komentaras.objects.create(diskusija=diskusija, gyventojas=gyventojas, turinys=turinys)
        return redirect('diskusija_perziureti', diskusijos_id=diskusijos_id)
    return render(request, 'prideti_komentara.html', {'diskusija': diskusija})

@login_required
def patinka_diskusija(request, diskusijos_id):
    diskusija = get_object_or_404(Diskusija, id=diskusijos_id)
    gyventojas = Gyventojas.objects.get(user=request.user)
    if gyventojas in diskusija.patikejai.all():
        diskusija.patikejai.remove(gyventojas)
    else:
        diskusija.patikejai.add(gyventojas)
    return redirect('diskusija_perziureti', diskusijos_id=diskusijos_id)