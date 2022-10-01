from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .validators import validate_contact_number

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager
    """
    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError('Blank Username not allowed')
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and save a SuperUser
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    is_hospital = models.BooleanField(default=False)
    ph_no = models.CharField(max_length=10, validators=[validate_contact_number], blank=False, unique=True)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email', 'ph_no']

    objects = CustomUserManager()

    def __str__(self):
        return super().__str__()


class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False)
    location = models.URLField(blank=False)

    def __str__(self):
        return str(self.user)


class PublicUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return str(self.user)



