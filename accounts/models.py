from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_contact_number

# Create your models here.


class User(AbstractUser):
    is_hospital = models.BooleanField(default=False)
    ph_no = models.CharField(max_length=10, validators=[validate_contact_number])
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email', 'ph_no']

    def __str__(self):
        return super().__str__()


class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False)
    address = models.CharField(blank=False)
    location = models.URLField(blank=False)

    def __str__(self):
        return str(user)


class PublicUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False)



