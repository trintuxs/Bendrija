

from django.urls import path

from gyventojas import views

urlpatterns = [
    path('flat/', views.flat, name='butas'),
    path('', views.index, name='index'),
    path('resident/', views.residents, name='gyventojas'),
    path('resident/', views.ResidentListView.as_view(), name='gyventojas'),
    path('register/', views.register, name='register'),
    ]