from django.db import models

from baseapp.models import BaseModel

CONTACT = [
    (1, 'one'), (2, 'two'), (3, 'third'),
    (4, 'four'), (5, 'five'),

]


class Contact(BaseModel):
    full_name = models.CharField(max_length=50, verbose_name="Foydalanuvchi ismi")
    email = models.EmailField(max_length=100, verbose_name="Email")
    place = models.IntegerField(choices=CONTACT, default=1)
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Kontakt"


class Footer(models.Model):
    number = models.CharField(max_length=100, verbose_name="telefon raqam")
    email = models.EmailField(max_length=100, verbose_name="email")
    location = models.CharField(max_length=255, verbose_name="manzil")
    longitude = models.FloatField(verbose_name="manzil kodi")
    latitude = models.FloatField(verbose_name="latitude")
    created_at = models.DateTimeField()

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "footer qismida malumotlar"
# Create your models here.
