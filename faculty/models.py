from django.db import models

# Create your models here.
class faculty(models.Model):
    username=models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
class meta:
    db_table:"faculty_faculty"
class facultysignup(models.Model):
    username=models.CharField(max_length=30,null=True,blank=True)
    designation=models.CharField(max_length=20)
    joindate=models.DateField(max_length=10)
    qualification=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    number=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=20)
    batch=models.CharField(max_length=20)
    blood=models.CharField(max_length=20)
    dob=models.DateField(max_length=10)
    address=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class meta:
    db_table:"faculty_facultysignup"
