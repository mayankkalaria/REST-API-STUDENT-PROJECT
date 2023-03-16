from django.db import models

# Create your models here.

class Student(models.Model):
	fname=models.CharField(max_length=100,blank=True)
	lname=models.CharField(max_length=100,blank=True)
	email=models.EmailField(blank=True)
	mobile=models.CharField(max_length=100,blank=True)
	course=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.fname+""+self.lname

