from django.db import models

from baseapp.models import BaseModel
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(BaseModel):
    theme = models.CharField(max_length=100, verbose_name='nomi')
    title = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.theme
    # def get_absolute_url(self):
    #     return "/"+str(self.id)+"/"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Blog'


# Create your models here.
