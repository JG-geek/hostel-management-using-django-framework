from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class student_details(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=30)
    father_occupation=models.CharField(max_length=30)
    mother_name=models.CharField(max_length=30)
    mother_occupation=models.CharField(max_length=30)
    current_address=models.CharField(max_length=100)
    permanent_address=models.CharField(max_length=100)
    date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
    age=models.PositiveIntegerField()
    contact_number=models.CharField(max_length=10)
    gender_type=models.TextChoices('gender_type', 'Male Female')
    gender=models.CharField(choices=gender_type.choices, max_length=10)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=10)

    
class hostel_rooms(models.Model):
    room_no=models.IntegerField(primary_key=True)
    person1=models.CharField(max_length=30)
    person2=models.CharField(max_length=30)
    person3=models.CharField(max_length=30)
    room=models.TextChoices('room', 'standard deluxe superdelux')
    room_type=models.CharField(choices=room.choices, max_length=10)
    building_no=models.CharField(max_length=2,blank=True)
    
