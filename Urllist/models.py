from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# from djoser.urls.base import User



class Links(models.Model):
    #  Model Rooms

    creater = models.ForeignKey(User, verbose_name="Creater", on_delete=models.CASCADE)
    url = models.CharField("URLS", max_length=200)
    status=models.IntegerField()
    date = models.DateTimeField("Date created", auto_now_add=True)


    class Meta:
        verbose_name="Link status"
        verbose_name_plural="Links status"
