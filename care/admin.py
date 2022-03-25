from django.contrib import admin
from .models import Client, Therapist

# Register your models here.
admin.site.register(Client)
admin.site.register(Therapist)