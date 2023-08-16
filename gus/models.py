from django.utils import timezone
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.PositiveIntegerField(auto_created=True,unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username
    

class Services(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(default='default.png', upload_to='service_pics/')
    serviceCharge = models.PositiveIntegerField(max_length=5, null=True)
    content = models.TextField()
    is_available = models.BooleanField(default=True)



class ServiceRequest(models.Model):
    req_time = models.DateTimeField(auto_now_add=True)
    serviceType = models.OneToOneField(Services, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
