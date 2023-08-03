# Generated by Django 4.2.1 on 2023-07-30 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Butas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_nr', models.IntegerField(verbose_name='Buto numeris')),
                ('size_kv', models.IntegerField(verbose_name='Buto plotas kv')),
            ],
            options={
                'verbose_name': 'Butas',
                'verbose_name_plural': 'Butai',
            },
        ),
        migrations.CreateModel(
            name='Gyventojas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Vardas')),
                ('last_name', models.CharField(max_length=50, verbose_name='Pavardė')),
                ('email', models.CharField(max_length=50, verbose_name='Elektroninis paštas')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('flat_nr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='savininkas', to='gyventojas.butas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gyventojas',
                'verbose_name_plural': 'Gyventojai',
            },
        ),
    ]
