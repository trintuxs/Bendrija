from django.shortcuts import render, get_object_or_404, redirect

from gyventojas.models import Resident
from .models import Diskusija, Komentaras
from django.contrib.auth.decorators import login_required

def diskusija_perziureti(request, diskusijos_id):
    diskusija = get_object_or_404(Diskusija, id=diskusijos_id)
    komentarai = Komentaras.objects.filter(diskusija=diskusija)
    context = {'diskusija': diskusija, 'komentarai': komentarai}
    return render(request, 'diskusija_perziureti.html', context=context)

@login_required
def prideti_komentara(request, diskusijos_id):
    diskusija = get_object_or_404(Diskusija, id=diskusijos_id)
    if request.method == 'POST':
        turinys = request.POST['turinys']
        gyventojas = Resident.objects.get(user=request.user)
        Komentaras.objects.create(diskusija=diskusija, gyventojas=gyventojas, turinys=turinys)
        return redirect('diskusija_perziureti', diskusijos_id=diskusijos_id)
    return render(request, 'prideti_komentara.html', {'diskusija': diskusija})

@login_required
def patinka_diskusija(request, diskusijos_id):
    diskusija = get_object_or_404(Diskusija, id=diskusijos_id)
    gyventojas = Resident.objects.get(user=request.user)
    if gyventojas in diskusija.patinka.all():
        diskusija.patinka.remove(gyventojas)
    else:
        diskusija.patinka.add(gyventojas)
    return redirect('patinka_diskusija', diskusijos_id=diskusijos_id)