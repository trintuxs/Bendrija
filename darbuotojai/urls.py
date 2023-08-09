from django.urls import path

from darbuotojai import views

app_name = 'darbuotojai'

urlpatterns = [
    path('', views.darbuotojai_list, name='darbuotojai_list'),
    path('apmoketi/<int:owner_id>/', views.apmoketi, name='apmoketi'),
]