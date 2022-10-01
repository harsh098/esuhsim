from rest_framework import serializers
from .models import Hospital

class RegisterSerializerHospital(serializers.ModelSerializer):
    pass

class RegisterPublicUserSerializer(serializers.ModelSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    pass