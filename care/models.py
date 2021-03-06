import email
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Client(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  age = models.CharField(max_length=100)
  gender = models.CharField(max_length=100)
  purpose = models.CharField(max_length=100)

  def save_name(self):
        self.save()

  def delete_client(self):
        self.delete()
      
  def __str__(self) -> str:
    return self.name
    

class Therapist(models.Model):
  # image = models.ImageField()
  id= models.IntegerField(primary_key=True)
  name = models.CharField(max_length= 200)
  age = models.CharField(max_length=1000)
  gender= models.CharField(max_length=300)
  experience= models.CharField(max_length=50)
  email= models.EmailField()
  speciality = models.CharField(max_length=300)
  
  def save_therapist(self):
        self.save()

  @classmethod
  def update_therapist(cls, id, value):
        therapist = cls.objects.filter(id=id).update(value=value)
        return therapist

  @classmethod
  def get_therapist_by_id(cls, id):
        therapist = cls.objects.filter(id=id).all()
        return therapist

  @classmethod
  def search_by_therapist(cls, therapist):
        therapist = cls.objects.filter(therapist__name__icontains=therapist)
        return therapist

  def __str__(self) -> str:
      return self.name


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
      return self.username 

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
      if created:
        Profile.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()