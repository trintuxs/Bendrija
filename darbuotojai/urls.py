from django.urls import path

from darbuotojai import views

urlpatterns = [
    path('', views.staff_list, name='staff_list')
   ]
