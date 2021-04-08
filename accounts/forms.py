from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.forms.widgets import DateInput, MultiWidget, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member

        fields = (
        'first_name', 'last_name', 'email_id', 'dob', 'phone_no', 'alt_phone_no', 'gender', 'address', 'fitness',
        'plan', 'trainer')
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
            # 'fitness': forms.CheckboxSelectMultiple(attrs={'required': True, 'style':'width:15px;height:15px;'}),
            # 'trainer': forms.RadioSelect(attrs={'required': True, 'style': 'width:15px;height:15px;'}),
            # 'plan': forms.RadioSelect(attrs={'required': True, 'style': 'width:15px;height:15px;'})
        }


class MyProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'dob', 'phone_no', 'alt_phone_no', 'gender', 'address', 'fitness')
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }
        exclude = ['user']


class FreeTrialForm(forms.ModelForm):
    class Meta:
        model = FreeTrial
        fields = ('first_name', 'last_name', 'dob', 'phone_no', 'alt_phone_no', 'email_id')
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email_id', 'message')
