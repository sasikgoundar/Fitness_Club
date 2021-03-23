from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member
from django import forms
from django.forms.widgets import DateInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2' ]


class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'email_id', 'dob', 'phone_no', 'alt_phone_no', 'gender', 'address', 'fitness', 'plan')
        widgets ={
            'dob': DateInput(attrs={'type': 'date'})
        }
