from django.contrib import admin
from django.urls import path
from administracija import views



urlpatterns = [
    path('', views.kaupiamasis_inasas, name='kaupiamasis_inasas'),

    path('admin/', admin.site.urls),
] 