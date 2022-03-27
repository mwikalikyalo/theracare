from dataclasses import field
from django import forms
from .models import Client, Therapist, Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
      model = Profile
      fields = ['username','bio','email']

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = '__all__'

class TherapistForm(forms.ModelForm):
  class Meta:
    model = Therapist
    fields = '__all__'