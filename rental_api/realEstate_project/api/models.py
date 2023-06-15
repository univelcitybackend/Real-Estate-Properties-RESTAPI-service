from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
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
<<<<<<< HEAD
    property_type = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
=======
>>>>>>> c12415305d1be4ff6baec1dd1c20526c2c68b374
    location = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    owner = models.ForeignKey(Agent, on_delete=models.CASCADE)


class Comment(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_text

