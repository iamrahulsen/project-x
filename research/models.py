from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Domain(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class Professor(models.Model):
    choices=(
        ('yes','yes'),
        ('no','no')
    )
    gen=(
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    marry=(
        ('married','married'),
        ('single','single')
    )
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    middle_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    college=models.CharField(max_length=100,null=True,blank=True)
    profile_pic=models.ImageField(default="avatar.png",blank=True,null=True)
    working=models.ManyToManyField(Domain,blank=True)
    available=models.BooleanField(null=True,blank=True,default=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,choices=gen,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    country=CountryField(blank=True,null=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    zip=models.CharField(max_length=10,null=True,blank=True)
    Degree=models.CharField(max_length=100,null=True,blank=True)
    experience=models.IntegerField(null=True,blank=True)
    marital_status=models.CharField(max_length=100,null=True,blank=True,choices=marry)
    fellowship=models.CharField(max_length=100,null=True,blank=True)
    number_of_papers=models.IntegerField(null=True,blank=True,default=0)
    notable_work=models.TextField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return "/signin_mentor/mentor/%i/" % self.id

class Student(models.Model):
    gen=(
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    middle_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    college=models.CharField(max_length=100,null=True,blank=True)
    working=models.ManyToManyField(Domain,blank=True)
    profile_pic=models.ImageField(default="avatar.png",null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,choices=gen,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    country=CountryField(blank=True,null=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    zip=models.CharField(max_length=10,null=True,blank=True)
    graduation_year=models.DateField(null=True,blank=True)
    Degree=models.CharField(max_length=100,null=True,blank=True)
    cgpa=models.FloatField(blank=True,null=True)
    experience=models.IntegerField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True,default=0)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return "/signin_student/student/%i/" % self.id

class Certificate(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    certificate_title=models.CharField(max_length=100,null=True,blank=True)
    certificate_description=models.CharField(max_length=100,null=True,blank=True)
    certificate_organisation=models.CharField(max_length=100,null=True,blank=True)
    certificate_ID=models.CharField(max_length=100,null=True,blank=True)
    certificate_url=models.CharField(max_length=100,null=True,blank=True)
    certificate_issue=models.DateField(null=True,blank=True)
    certificate_expire=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.student.username

class Project(models.Model):
    status=(
        ('stall','stall'),
        ('ongoing','ongong'),
        ('finished','finished')
    )
    name=models.CharField(max_length=100,null=True)
    date_started=models.DateTimeField(auto_now_add=True,null=True)
    date_finished=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=100,choices=status,default='stall')
    students=models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
    mentors=models.ForeignKey(Professor,null=True,on_delete=models.CASCADE)
    description=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.mentors.username

    



