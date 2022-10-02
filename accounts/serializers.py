from rest_framework import serializers
from .models import Hospital, User, PublicUser


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicUser
        exclude = ['user', ]


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        exclude = ['user', ]


class RegisterPublicUserSerializer(serializers.ModelSerializer):
    publicUser = PublicUserSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'ph_no', 'publicUser', 'is_hospital']

    def create(self, validated_data):
        user_data = validated_data.pop('publicUser')
        user_instance = User.objects.create_user(**validated_data)
        PublicUser.objects.create(user=user_instance, **user_data)
        return user_instance


class RegisterHospitalSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'ph_no', 'hospital', 'is_hospital']

    def create(self, validated_data):
        hospital_data = validated_data.pop('hospital')
        user_instance = User.objects.create_user(**validated_data,is_hospital=True)
        Hospital.objects.create(user=user_instance, **hospital_data)
        return user_instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
