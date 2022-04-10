from atexit import register
from email.policy import default
from uuid import uuid4
from django.db import models
from users.models import Profiles

# Create your models here.

class Register(models.Model):
    owner=models.ForeignKey(Profiles,null=True,blank=True,on_delete=models.SET_NULL)
    full_name=models.CharField(max_length=200)
    intro=models.TextField(null=True,blank=True)
    value=(
        ('Instructor','Instructor'),
        ('Attendee','Attendee'),
    )
    member_type=models.CharField(max_length=100,choices=value,default='')

    id=models.UUIDField(default=uuid4,unique=True,primary_key=True,editable=False)

    #creating manny to Many relation with workshop_details model 
    Workshop_details=models.ManyToManyField('Workshop_details',blank=True)


    profile_pic = models.ImageField(null=True,blank=True,default='default.jpg')

    skill_set=models.CharField(max_length=2000,null=True,blank=True)
    reason=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.full_name

class Workshop_details(models.Model):
    workshop_name=models.CharField(max_length=2000,blank=True,null=True)
    workshop_date=models.CharField(max_length=200,blank=True,null=True)
    workshop_time=models.CharField(max_length=200,blank=True,null=True)
    workshop_subject=models.CharField(max_length=5000,null=True,blank=True)
    workshop_details=models.TextField(null=True,blank=True)
    id=models.UUIDField(default=uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.workshop_name



