from django.db import models

from baseapp.models import BaseModel

class Menu(BaseModel):
    category=(
        ("D",'DRINKS'),
        ("L",'LUNCH'),
        ("DI",'DINNER'),

    )
    menu_name = models.CharField(max_length=200)
    menu_about = models.TextField()
    menu_price = models.CharField(max_length=100)
    menu_image = models.ImageField(upload_to="image/")
    menu_category=models.CharField(max_length=10,choices=category)




    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Menu"
# Create your models here.
