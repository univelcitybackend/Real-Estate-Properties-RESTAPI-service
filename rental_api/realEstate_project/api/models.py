from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Agent(AbstractUser):
    email = models.EmailField(verbose_name="Email Address", max_length=225 , unique=True)

    REQUIRED_FIELDS=['username', 'first_name', 'last_name']
    USERNAME_FIELD="email"

    def get_username(self)  -> str:
        return self.email


class Property(models.Model):
    image = models.ImageField(verbose_name="Image", upload_to='property_images/')
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    owner = models.ForeignKey(Agent, on_delete=models.CASCADE)
