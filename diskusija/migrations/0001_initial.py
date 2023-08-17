# Generated by Django 4.2.1 on 2023-08-17 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diskusija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('text', models.TextField(verbose_name='Turinys')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Diskusija',
                'verbose_name_plural': 'Diskusijos',
            },
        ),
        migrations.CreateModel(
            name='Komentaras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turinys', models.TextField(verbose_name='Turinys')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('diskusija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diskusija.diskusija')),
            ],
            options={
                'verbose_name': 'Komentaras',
                'verbose_name_plural': 'Komentarai',
            },
        ),
    ]
