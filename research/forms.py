from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['name','students','status','mentors','description','date_finished']
    
class StudentUpdateInfo(ModelForm):
    class Meta:
        model=Student
        fields=['first_name','middle_name','last_name','email','phone','college','dob','gender','address','country','state','city','zip','profile_pic','graduation_year','Degree','cgpa','experience']

class MentorUpdateInfo(ModelForm):
    class Meta:
        model=Professor
        fields=['first_name','middle_name','last_name','email','phone','college','dob','gender','address','country','state','profile_pic','city','zip','available','Degree','marital_status','fellowship','number_of_papers','notable_work']
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

