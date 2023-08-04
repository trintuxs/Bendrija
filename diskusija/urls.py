from django.contrib import admin
from django.urls import path

from diskusija import views

urlpatterns = [
    path('diskusija/', views.diskusija_perziureti, name='diskusija_perziureti'),
    path('diskusija/<int:diskusijos_id>/komentaras/', views.prideti_komentara, name='prideti_komentara'),
    path('diskusija/<int:diskusijos_id>/patinka/', views.patinka_diskusija, name='patinka_diskusija'),

]