from django.db import models
import uuid
from accounts.models import Hospital


# Create your models here.

class Organtype(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def clean(self):
        self.name = self.name.lower()

    def __str__(self):
        return str(self.name)


class Organ(models.Model):
    organType = models.ForeignKey(Organtype, on_delete=models.CASCADE)

    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('NA', 'NA')

    ]
    bloodType = models.CharField(max_length=3, choices=BLOOD_TYPES, default='NA')

    age = models.IntegerField(blank=False, default=-1)      # -1 for age_NA
    SEX = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER'),
        ('NA', 'NOT AVAILABLE')
    ]
    sex = models.CharField(max_length=2, choices=SEX, default='NA')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return f'{str(self.hospital.name)}-{str(self.organType)}'


