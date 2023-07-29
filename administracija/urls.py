from django.contrib import admin
from django.urls import path
from administracija import views



urlpatterns = [
    path('', views.buto_inasai, name='buto_inasai'),
    path('admin/', admin.site.urls),
] 