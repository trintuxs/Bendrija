
from django.db import models

from gyventojas.models import Gyventojas


class Diskusija(models.Model):
    gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Pavadinimas")
    text = models.TextField(verbose_name="Turinys")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Diskusija'
        verbose_name_plural = 'Diskusijos'

class Komentaras(models.Model):
    diskusija = models.ForeignKey('Diskusija', on_delete=models.CASCADE)
    gyventojas = models.ForeignKey(Gyventojas, on_delete=models.CASCADE)
    turinys = models.TextField(verbose_name="Turinys")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gyventojas.first_name} {self.gyventojas.last_name}: {self.turinys}"

    class Meta:
        verbose_name = 'Komentaras'
        verbose_name_plural = 'Komentarai'