import email
from django.db import models

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
    return self.location_name

# Create your models here.
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
        therapist = cls.objects.filter(id=id).update(name=value)

  @classmethod
  def get_therapist_by_id(cls, id):
        therapist = cls.objects.filter(id=id).all()
        return therapist

  @classmethod
  def search_by_category(cls, category):
        therapist = cls.objects.filter(therapist__name__icontains=therapist)
        return therapist

  def __str__(self) -> str:
      return self.name


