# Generated by Django 4.2.6 on 2023-10-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='text3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]