from django.contrib import admin
from administracija.models import Kaupiamsis_Inasas, Expenses

# Register your models here.

class Kaupiamasis_InasasAdmin(admin.ModelAdmin):
    list_display = ('owner', 'amount')



admin.site.register(Kaupiamsis_Inasas, Kaupiamasis_InasasAdmin)
admin.site.register(Expenses)