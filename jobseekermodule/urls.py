from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'jobseekermodule'
urlpatterns = [
    path('viewjobs/', views.viewjobs, name='viewjobs'),
    path('job_details_list', views.job_details_list, name='job_details_list'),
    path('job_application_list/', views.job_application_list, name='job_application_list'),
    path('submit_application/', views.submit_application, name='submit_application'),

]
