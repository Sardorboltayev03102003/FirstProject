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

# Create your models here.
