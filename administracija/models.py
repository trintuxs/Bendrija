from django.core.mail import send_mail
from django.db import models
from django.db.models import Sum

from gyventojas.models import Butas
from datetime import date
# Create your models here.
class Kaupiamsis_Inasas(models.Model):
    owner = models.ForeignKey(Butas, on_delete=models.CASCADE)
    amount = models.FloatField(verbose_name="Inaso suma")
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Kaupiamasis Inasas: {self.owner} - {self.owner.size_kv} m² "

    #Apskaiciuojamas visų kaupiamųjų įnašų sumą pagal savininką
    @classmethod
    def calculate_total_amount(cls, owner):
        total_amount = cls.objects.filter(owner=owner).aggregate(Sum('amount'))['amount__sum']
        return total_amount if total_amount else 0

   #Kaupiamojo inaso sumos skaiciavimas
    def calculate_payment_amount(self):
        return self.owner.size_kv * 0.12

    #Pranesimo siuntimas
    def send_payment_email(self):
        subject = 'Mokėjimas už kaupiamąjį įnašą'
        message = f"Sveiki,\n\nPrašome apmokėti sumą {self.calculate_payment_amount()} už kaupiamąjį įnašą.\n\nPagarbiai,"
        from_email = 'ilgoji4bendrija@gmail.com'
        savininkas = self.owner.savininkas.first()  # Naudokite susijusio objekto 'related_name'
        if savininkas:
            recipient_list = [savininkas.user.email]  # Priėjimas prie gyventojo el. pašto
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    #Apskaiciuojama visu inasu suma
    @classmethod
    def calculate_total_sum(cls):
        total_sum = cls.objects.aggregate(Sum('amount'))['amount__sum']
        return total_sum if total_sum else 0

    class Meta:
        verbose_name = 'Kaupiamsis inasas'
        verbose_name_plural = 'Kaupiamieji Inasai'




class Islaidos(models.Model):
    discription = models.TextField(verbose_name=("Lėšų panaudojimas:"))
    repairs_cost = models.FloatField(verbose_name=("Išleista suma:"))
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.discription

  #Apskaiciuojama sio menesio islaidu suma
    @classmethod
    def calculate_total_current_month_expenses(cls):
        current_month = date.today().month
        total_current_month_expenses = cls.objects.filter(date__month=current_month).aggregate(Sum('repairs_cost'))[
            'repairs_cost__sum']
        return total_current_month_expenses if total_current_month_expenses else 0

    class Meta:
        verbose_name = 'Išlaidos'
        verbose_name_plural = 'Išlaidos'
