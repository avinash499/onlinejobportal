from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('employerhomepage', views.employerhomepage, name='employerhomepage'),
    path('jobseekerhomepage', views.jobseekerhomepage, name='jobseekerhomepage'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('signup1', views.signup1, name='signup1'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('company', views.company, name='company'),
    path('read', views.read, name='read'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('account_details', views.account_details, name='account_details'),
    path('user_profile', views.user_profile, name='user_profile'),

]
