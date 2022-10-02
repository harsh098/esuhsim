from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterPublicUserSerializer, RegisterHospitalSerializer
from .models import User
# Create your views here.


class RegisterHospital(generics.CreateAPIView):
    serializer_class = RegisterHospitalSerializer
    queryset = User.objects.all()


class RegisterPublicUser(generics.CreateAPIView):
    serializer_class = RegisterPublicUserSerializer
    queryset = User.objects.all()




