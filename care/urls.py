from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('client/',views.ClientApi, names="clientapi"),
    path('therapist/',views.therapistApi, names="therapistApi"),
]