from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    path('client/',views.clientApi, names="clientapi"),
    path('therapist/',views.therapistApi, names="therapistApi"),
]