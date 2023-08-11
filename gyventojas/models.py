
from django.contrib.auth.models import User, AbstractUser
from django.db import models



# Create your models here.


class Resident(AbstractUser):

    first_name = models.CharField(max_length=50, verbose_name="Vardas")
    last_name = models.CharField(max_length=50, verbose_name="Pavardė")
    email = models.CharField(max_length=50, verbose_name="Elektroninis paštas")
    flat_nr = models.ForeignKey('Flat', on_delete=models.SET_NULL, null=True, blank=True, related_name='savininkas')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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


