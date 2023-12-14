from django.db import models

from baseapp.models import BaseModel


class Menu(BaseModel):
    category = (
        ("drinks", 'DRINKS'),
        ("lunch", 'LUNCH'),
        ("dinner", 'DINNER'),

    )
    menu_name = models.CharField(max_length=200)
    menu_about = models.TextField()
    menu_price = models.CharField(max_length=100)
    menu_image = models.ImageField(upload_to="image/")
    menu_category = models.CharField(max_length=10, choices=category, default='dinner')

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Menu"


class Menu_Customer(BaseModel):
    image = models.ImageField(upload_to="media")
    name = models.CharField(max_length=100)
    jobs = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer revirse_"

# Create your models here.
