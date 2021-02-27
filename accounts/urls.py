from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,  name="Homepage"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('member/', views.member, name='member'),
    path('trainer/', views.trainer, name='trainer'),
    path('about/', views.about, name='Aboutus'),
    path('myprofile', views.myprofile, name= 'MyProfile')
]