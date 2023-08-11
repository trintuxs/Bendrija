from django.urls import path

from darbuotojai import views



urlpatterns = [
    path('', views.staff_list, name='darbuotojai_list'),

]