from django.db import models

from baseapp.models import BaseModel

person = [
    (1, 'one'), (2, 'two'), (3, 'third'),
    (4, 'four'), (5, 'five'), (6, 'six'),
    (7, 'seven'),

]


class Reservation(BaseModel):
    data = models.DateField()
    name = models.CharField(max_length=50, verbose_name="Foydalanuvchi ismi")
    email = models.EmailField(max_length=100, verbose_name="Email")
    place = models.IntegerField(choices=person, default=1)
    number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Joy buyurtma qilish"


class Stuff(BaseModel):
    name = models.CharField(max_length=100, verbose_name="oshpazni ismi")
    image = models.ImageField(upload_to='image/')
    job = models.CharField(max_length=100, verbose_name="oshpazni turi")
    l_google = models.URLField()
    l_facebook = models.URLField()
    l_twitter = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Oshpazlar haqida malumot'


class Gallery(BaseModel):
    image = models.ImageField(upload_to="image/")

    class Meta:
        verbose_name = "Taomlarni rasmi"

# Create your models here.
