from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.


class Resident(AbstractUser):
    flat_nr = models.ForeignKey('Flat', on_delete=models.SET_NULL, null=True, blank=True, related_name='butas')



    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.flat_nr} {self.email}"

    class Meta:
        verbose_name = 'Resident'
        verbose_name_plural = 'Residents'


class Flat(models.Model):
    flat_nr = models.IntegerField(verbose_name="Buto numeris")
    size_kv = models.IntegerField(verbose_name="Buto plotas kv")
    owner = models.ForeignKey(Resident, on_delete=models.SET_NULL, null=True, blank=True, related_name='savininkas')

    def __str__(self):
        return f"{self.flat_nr} {self.size_kv}"

    class Meta:
        verbose_name = 'Flat'
        verbose_name_plural = 'Flats'
