from django.db import models
from gyventojas.models import Butas
from datetime import date
# Create your models here.
class Kaupiamsis_Inasas(models.Model):
    owner = models.ForeignKey(Butas, on_delete=models.CASCADE)
    amount = models.FloatField(verbose_name="Inaso suma")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Kaupiamasis Inasas: {self.owner} - {self.amount}"

    class Meta:
        verbose_name = 'Kaupiamsis inasas'
        verbose_name_plural = 'Kaupiamieji Inasai'


class Islaidos(models.Model):
    discription = models.TextField(verbose_name=("Lėšų panaudojimas:"))
    repairs_cost = models.FloatField(verbose_name=("Išleista suma:"))
    date = models.DateField(default=date.today)
    def __str__(self):
        return self.discription

    class Meta:
        verbose_name = 'Išlaidos'
        verbose_name_plural = 'Išlaidos'
