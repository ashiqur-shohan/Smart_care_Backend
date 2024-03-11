from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=30)
    #jehetu filter krbo tar jonno slug field lgbe ta chara filter kora jabe na
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=30)
    #jehetu filter krbo tar jonno slug field lgbe ta chara filter kora jabe na
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name


# one to many te -> many part a foreign key ta add korte hoy
class AvailableTime(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

# ekhane bhul kore felsi. onk pera neyar theke time take  many to many banay felaisi.
    # field ta deyar kotha chilo available time a 
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    #ekhane one to many o use kora jaito but jehetu filter korbo tai easy korar jonno many to many use kora hoyeche
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField()
    rating = models.CharField(choices = STAR_CHOICES,max_length=10)

    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name} ; Doctor : {self.doctor.user.first_name}"