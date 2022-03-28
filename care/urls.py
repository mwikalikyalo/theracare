from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    path('create/profile/',views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('find/', views.find, name='search'),
    path('therapy/', views.therapy, name='profile'),
    path('client/',views.clientApi, name="clientapi"),
    path('therapist/',views.therapistApi, name="therapistApi"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)