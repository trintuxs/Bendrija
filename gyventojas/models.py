from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Gyventojas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="Vardas")
    last_name = models.CharField(max_length=50, verbose_name="Pavardė")
    email = models.CharField(max_length=50, verbose_name="Elektroninis paštas")
    flat_nr = models.ForeignKey('Butas', on_delete=models.SET_NULL, null=True, related_name='savininkas')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Gyventojas'
        verbose_name_plural = 'Gyventojai'


class Butas(models.Model):
    flat_nr = models.IntegerField(verbose_name="Buto numeris")
    size_kv = models.IntegerField(verbose_name="Buto plotas kv")

    def __str__(self):
        return f"{self.flat_nr} {self.size_kv}"

    class Meta:
        verbose_name = 'Butas'
        verbose_name_plural = 'Butai'
