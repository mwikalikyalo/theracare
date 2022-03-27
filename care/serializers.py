from dataclasses import fields
from rest_framework import serializers
from .models import Client, Therapist

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields= ( 'name'
                  'email'
                  'age'
                  'gender'
                  'purpose')

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        exclude= 'age'