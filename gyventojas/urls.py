

from django.urls import path

from gyventojas import views

urlpatterns = [
    path('butas/', views.butas, name='butas'),
    path('', views.index, name='index'),
    path('gyventojas/', views.gyventojai, name='gyventojas'),
    path('gyventojas/', views.GyventojasListView.as_view(), name='gyventojas'),
    path('register/', views.register, name='register'),
    ]