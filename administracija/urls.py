
from django.urls import path
from administracija import views



urlpatterns = [
    path('', views.kaupiamasis_inasas, name='kaupiamasis_inasas'),
]