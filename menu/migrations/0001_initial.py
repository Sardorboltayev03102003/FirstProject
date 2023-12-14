# Generated by Django 4.2.6 on 2023-12-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu_name', models.CharField(max_length=200)),
                ('menu_about', models.TextField()),
                ('menu_price', models.CharField(max_length=100)),
                ('menu_image', models.ImageField(upload_to='image/')),
                ('menu_category', models.CharField(choices=[('D', 'DRINKS'), ('L', 'LUNCH'), ('DI', 'DINNER')], max_length=10)),
            ],
            options={
                'verbose_name': 'Menu',
            },
        ),
    ]
