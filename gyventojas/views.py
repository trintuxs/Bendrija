from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_protect

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


def gyventojai(request):
    gyventojas = Gyventojas.objects.all()
    return render(request, 'gyventojas.html', {'gyventojas': gyventojas})


class GyventojasListView(generic.ListView):
    model = Gyventojas
    template_name = 'gyventoju_sarasas.html'

def butas(request):
    butas = Butas.objects.all()
    context = {
        'butas': butas
    }
    print(butas)
    return render(request, 'butas.html', context)

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')