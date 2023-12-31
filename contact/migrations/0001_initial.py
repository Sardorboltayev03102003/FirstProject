# Generated by Django 4.2.6 on 2023-12-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=50, verbose_name='Foydalanuvchi ismi')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('place', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'third'), (4, 'four'), (5, 'five')], default=1)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Kontakt',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='telefon raqam')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('location', models.CharField(max_length=255, verbose_name='manzil')),
                ('longitude', models.FloatField(verbose_name='manzil kodi')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'footer qismida malumotlar',
            },
        ),
    ]
