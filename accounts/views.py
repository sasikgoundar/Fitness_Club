from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm

@login_required(login_url='login')
def member(request):
    members = Member.objects.all()
    total_members = members.count()
    trainers = Trainer.objects.all()
    total_trainers = trainers.count()
    return render(request, 'accounts/member.html', {'members': members, 'trainers':trainers, 'total_members': total_members, 'total_trainers':total_trainers})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Homepage')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')


    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Homepage')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def trainer(request):
    return render(request, 'accounts/trainer.html')


def homepage(request):
    return render(request, 'accounts/homepage.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'accounts/about.html')

@login_required(login_url='login')
def myprofile(request):
    return render(request, 'accounts/my_profile.html')


