from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Domain)
admin.site.register(Project)
