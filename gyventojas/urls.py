
from django.contrib import admin
from django.urls import path

from gyventojas import views

urlpatterns = [
    path('butas/', views.butas, name='butas'),
    path('', views.index, name='index'),
    path('gyventojas/', views.gyventojas, name='gyventojas'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
]