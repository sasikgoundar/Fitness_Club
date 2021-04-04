from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .views import LandingPageView

urlpatterns = [
    path('', views.homepage,  name="Homepage"),
    path('home', views.afterlogin,  name="Afterlogin"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('user/', views.userPage, name="user-page"),
    path('logout/', views.logoutUser, name="logout"),
    path('member/', views.member, name='member'),
    path('trainer/', views.trainer, name='trainer'),
    path('about/', views.about, name='Aboutus'),
    path('myprofile/', views.myprofile, name= 'MyProfile'),
    path('membership/', views.createmember, name= 'Membership'),
    path('myprofile_update/', views.accountsettings, name= 'ProfileUpdate'),
    path('faq/', views.faq, name= 'Faq'),
    path('privacy_policy/', views.privacypolicy, name= 'PrivacyPolicy'),
    path('terms/', views.terms, name= 'Terms'),
    path('attendance/', views.attendance, name= 'Attendance'),
    path('land/', LandingPageView.as_view(), name='Landing'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),

    path('activate/<uidb64>/<token>/',views.activate, name='activate'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
]
