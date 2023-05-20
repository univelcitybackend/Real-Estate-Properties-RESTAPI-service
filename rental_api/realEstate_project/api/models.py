from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Agent(AbstractUser):
    email = models.EmailField(verbose_name="Email Address", max_length=225 , unique=True)

    REQUIRED_FIELDS=['username', 'first_name', 'last_name']
    USERNAME_FIELD="email"

    def get_username(self)  -> str:
        return self.email
