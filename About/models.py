from django.db import models
from baseapp.models import BaseModel


class About(BaseModel):
    name = models.CharField(max_length=200, verbose_name="teks nomi")
    image = models.ImageField(upload_to="image/")
    text = models.TextField()
    body=models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Restoran haqida malumot"

# Create your models here.


# Create your models here.
