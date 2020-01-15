from django.db import models

# Create your models here.

class students(models.Model):
    admno=models.CharField(max_length=30,null=True,blank=True)
    name=models.CharField(max_length=20)
    rollno=models.DateField(max_length=10)
    qualification=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    batch=models.CharField(max_length=20)
    dob=models.DateField(max_length=10)
    admdate=models.DateField(max_length=30)
    blood=models.CharField(max_length=20,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=20,blank=True)
    religion=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    password=models.CharField(max_length=20,null=True,blank=True)


    class meta:
      db_table:"student"
