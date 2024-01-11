from django.db import models
from django import forms
from django.core import validators

# Create your models here.

def letter(data):
    if data.lower()[0]=='a':
        raise forms.ValidationError('starts with a')



class Student(models.Model):
    Sname=models.CharField(max_length=20,validators=[letter])
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    def __str__(self):
        return self.Sname