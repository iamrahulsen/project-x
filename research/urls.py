from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup_student/',views.signup_student,name='signup_student'),
    path('signup_mentor/',views.signup_mentor,name='signup_mentor'),
    path('signin_student/',views.signin_student,name='signin_student'),
    path('signin_mentor/',views.signin_mentor,name='signin_mentor'),
    path('student_logout/',views.StudentLogout,name='student_logout'),
    path('mentor_logout/',views.MentorLogout,name='mentor_logout'),
    path('signin_mentor/mentor/<str:pk>/',views.mentor,name='mentor'),
    path('signin_student/student/<str:pk>/',views.student,name='student'),
    path('new_project/<str:pk>/',views.new_project,name='new_project'),
    path('edit_project/<str:pk>/',views.edit_project,name='edit_project'),
    path('student_profile/<str:pk>/',views.student_profile,name='student_profile'),
    path('mentor_profile/<str:pk>/',views.mentor_profile,name='mentor_profile'),
]