from django.contrib import admin
from gyventojas.models import Gyventojas, Butas


class GyventojasAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'flat_nr')


class ButasAdmin(admin.ModelAdmin):
    list_display = ('flat_nr', 'size_kv')





# Register your models here.
admin.site.register(Gyventojas, GyventojasAdmin)
admin.site.register(Butas, ButasAdmin)

