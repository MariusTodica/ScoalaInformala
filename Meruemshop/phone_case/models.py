
from django.db import models
from users.models import AuthUser
from PIL import Image


class Case(models.Model):
    name = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name} - {self.material} - {self.color} - {self.image} - {self.price} - {self.stock}"

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 150:
            new_img = (200, 150)
            img.thumbnail(new_img)
            img.save(self.image.path)


class Logs_Cases(models.Model):

    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
