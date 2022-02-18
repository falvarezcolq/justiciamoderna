"""Lawyer Serializer"""
# Django
from django.utils.translation import ugettext_lazy as _

# Django REST Framework
from rest_framework import serializers,exceptions
from rest_framework.serializers import ValidationError


class LawyerCreateSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    dni = serializers.CharField(max_length=32)
    cellphone = serializers.CharField(  max_length=32)
    telephone = serializers.CharField(  max_length=32)
    address = serializers.CharField(  max_length=255)
    matricula = serializers.CharField()
    region = serializers.IntegerField()






