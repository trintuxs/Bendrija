from django.db import models

# Create your models here.
class Staff(models.Model):
    duties = models.CharField(max_length=200, verbose_name='Pareigos')
    wage = models.FloatField(verbose_name='Darbo užmokestis')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.duties} {self.wage} "




#darbo uzmokestis pagal pareigas
    def save(self, *args, **kwargs):
        if self.duties == 'Komendantas':
            self.wage = 100
        elif self.duties == 'Buhaltere':
            self.wage = 50
        elif self.duties == 'Valytoja':
            self.wage = 25
        super(Staff, self).save(*args, **kwargs)
