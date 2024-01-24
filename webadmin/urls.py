from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('my-courses', views.my_courses, name='my_courses'),
    path('lessons/<str:slug>', views.lessons, name='lessons'),
    path('<str:slug>', views.course, name='course'),
]