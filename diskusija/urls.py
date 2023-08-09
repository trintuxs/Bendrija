from django.urls import path
from diskusija import views

urlpatterns = [
    path('<int:diskusijos_id>/', views.diskusija_perziureti, name='diskusija_perziureti'),
    path('<int:diskusijos_id>/komentaras/', views.prideti_komentara, name='prideti_komentara'),
    path('<int:diskusijos_id>/patinka/', views.patinka_diskusija, name='patinka_diskusija'),
]