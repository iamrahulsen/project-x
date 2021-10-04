from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group


def index(request):
    return render(request,'index.html')

@login_required(login_url='signin_student')
@admin_only
def home(request):
    return render(request,'home.html')

@login_required(login_url='signin_mentor')
def mentor(request,pk):
    mentor=Professor.objects.get(id=pk)
    name=mentor.username
    req_user=str(request.user)
    domains= mentor.working.all()
    projects=mentor.project_set.all()
    project_req=mentor.project_set.filter(status="stall").count()
    finished=mentor.project_set.filter(status="finished").count()
    rating=finished*100
    count=projects.count()
    context={'mentor':mentor,'count':count,'projects':projects,'domains':domains,'name':name,'request':project_req,'user':req_user,'rating':rating}
    return render(request,'mentor.html',context)
@login_required(login_url='signin_mentor')
@allowed_users(allowed_roles=['Mentor'])
def mentor_profile(request,pk):
    mentor=Professor.objects.get(id=pk)
    form=MentorUpdateInfo(instance=mentor)
    if request.method=='POST':
        form=MentorUpdateInfo(request.POST,request.FILES,instance=mentor)
        if form.is_valid():
            form.save()
            return redirect(mentor)
        else:
            messages.info(request,"Unsuccessful")
    context={'form':form,'id':pk}
    return render(request,'mentor_profile.html',context)

@login_required(login_url='signin_student')
def student(request,pk):
    student=Student.objects.get(id=pk)
    name=student.username
    domains=student.working.all()
    projects=student.project_set.all()
    count=projects.count()
    ongoing=student.project_set.filter(status="ongoing").count()
    finished=student.project_set.filter(status="finished").count()
    rating=finished*100
    context={'student':student,'domains':domains,'projects':projects,'count':count,'ongoing':ongoing,'finished':finished,'name':name,'rating':rating}
    return render(request,'student.html',context)


@login_required(login_url='signin_student')
def new_project(request,pk):
    student=Student.objects.get(id=pk)
   # initial_data={'Students':student[0].name}
    form=ProjectForm(initial={'students':student})
    if request.method=='POST':
        form=ProjectForm(request.POST)
        choose=request.POST['mentors']
        mentor_choose=Professor.objects.filter(id=choose)
        if not mentor_choose[0].available:
            messages.info(request,"Mentor not available")
        else:
            form=ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                #path='signin_student/student/'+str(pk)+"/"
                return redirect(student)
    context={'form':form}
    return render(request,'new_project.html',context)

def edit_project(request,pk):
    project=Project.objects.get(id=pk)
    mentor_id=project.mentors.id
    mentor=Professor.objects.get(id=mentor_id)
    form=ProjectForm(instance=project)
    if request.method=="POST":
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            
            form.save()
            return redirect(mentor)
    context={'form':form}
    return render(request,'new_project.html',context)


@login_required(login_url='signin_student')
@allowed_users(allowed_roles=['Student'])
def student_profile(request,pk):
    student=Student.objects.get(id=pk)
    form=StudentUpdateInfo(instance=student)
    if request.method=='POST':
        form=StudentUpdateInfo(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect(student)
            messages.success(request,"Successfully Updated")
        else:
            messages.info(request,"Unsuccessful")
    context={'form':form}
    return render(request,'student_profile.html',context)



@unauthenticated_user
def signup_student(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name="Student")
            user.groups.add(group)
            new=Student.objects.create(
                user=user,
                username=user.username,
                email=user.email
            )
            return redirect('signin_student')
    context={'form':form}
    return render(request,'signup_student.html',context)

@unauthenticated_user
def signup_mentor(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name="Mentor")
            user.groups.add(group)
            new=Professor.objects.create(
                user=user,
                username=user.username,
                email=user.email
            )
            return redirect('signin_mentor')
        else:
            messages.warning(request,"Unsuccessful")
    context={'form':form}
    return render(request,'signup_mentor.html',context)

@unauthenticated_user
def signin_student(request):
    context={}
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            new=Student.objects.get(username=username)
            new_id=new.id
            print(new_id)
            path='student/'+str(new.id)+"/"
            login(request,user)
            #messages.success(request,"Logged In")
            return redirect(path)
        else:
            messages.info(request,"Username OR Password Incorrect")
            return render(request,'signin_student.html',context)
            #return redirect('home')
    
    return render(request,'signin_student.html',context)

@unauthenticated_user
def signin_mentor(request):
    context={}
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            new=Professor.objects.get(username=username)
            path='mentor/'+str(new.id)+"/"
            login(request,user)
            return redirect(path)
        else:
            messages.info(request,"Username OR Password Incorrect")
            return render(request,'signin_mentor.html',context)
            #return redirect('home')
    
    return render(request,'signin_mentor.html',context)

@login_required(login_url='signin_student')
def StudentLogout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='signin_mentor')
def MentorLogout(request):
    logout(request)
    return redirect('index')