from django.db import models
from django.db.models import Sum


# Create your models here.
class Staff(models.Model):
    duties = models.CharField(max_length=200, verbose_name='Pareigos')
    wage = models.FloatField(verbose_name='Darbo užmokestis')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.duties} {self.wage} "





