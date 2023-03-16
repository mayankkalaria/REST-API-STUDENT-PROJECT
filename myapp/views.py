from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import Studentserializer

# Create your views here.

class StudentList(generics.ListCreateAPIView):
	queryset=Student.objects.all()
	serializer_class=Studentserializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Student
	serializer_class=Studentserializer


