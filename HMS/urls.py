from django.conf.urls import url
from HMS import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.get, name='get'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/homeview/', views.homeview, name='homeview'),
    path('register/personaldetails', views.personaldetails, name='personaldetails'),
    path('register/vacantroom', views.vacantroom, name='vacantroom'),
    path('register/bookroom', views.bookroom, name='bookroom'),
    path('myroom/', views.myroom, name='myroom'),
    path('mail/', views.mail, name='mail'),
]
