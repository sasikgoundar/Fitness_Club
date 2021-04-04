from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import transaction
import stripe
from django.views import View
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import *
from .forms import CreateUserForm, MemberCreateForm, MyProfileForm
from .decorators import unauthenticated_user, allowed_users

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


@login_required(login_url='login')
def createmember(request):
    if request.method == 'POST':
        form = MemberCreateForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            context ={'form': form}
            return redirect('Landing')

    else:
        form = MemberCreateForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/member_register.html', context)


@login_required(login_url='login')
def member(request):
    members = Member.objects.all()
    total_members = members.count()
    trainers = Trainer.objects.all()
    total_trainers = trainers.count()
    return render(request, 'accounts/member.html',
                  {'members': members, 'trainers': trainers, 'total_members': total_members,
                   'total_trainers': total_trainers})


def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)


"""@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')


    context = {'form':form}
    return render(request, 'accounts/register.html', context)"""

unauthenticated_user


def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='Member')
            user.groups.add(group)
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'accounts/email_verify_done.html')
    else:
        return HttpResponse('Activation link is invalid!')


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Afterlogin')
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


@login_required(login_url='login')
def afterlogin(request):
    return render(request, 'accounts/afterlogin_fitness.html')


def homepage(request):
    members = Member.objects.all()
    total_members = members.count()
    trainers = Trainer.objects.all()
    total_trainers = trainers.count()
    return render(request, 'accounts/fitness_homepage.html',
                  {'members': members, 'trainers': trainers, 'total_members': total_members,
                   'total_trainers': total_trainers})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Trainer'])
def attendance(request):
    return render(request, 'accounts/attendance.html')


def about(request):
    return render(request, 'accounts/about.html')


def faq(request):
    return render(request, 'accounts/faq_fitness.html')


def privacypolicy(request):
    return render(request, 'accounts/privacy_policy.html')


def terms(request):
    return render(request, 'accounts/terms.html')


@login_required(login_url='login')
def myprofile(request):
    datas = Member.objects.filter(user=request.user)
    return render(request, 'accounts/my_profile.html', {'data': datas})


@login_required(login_url='login')
def accountsettings(request):
    member = request.user.member
    form = MyProfileForm(instance=member)

    if request.method == 'POST':
        form = MyProfileForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('MyProfile')

    context = {'form': form}
    return render(request, 'accounts/my profile_update.html', context)

from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView

class LandingPageView(TemplateView):
    template_name = 'accounts/landing.html'


class SuccessView(TemplateView):
    template_name = 'accounts/success.html'


class CancelledView(TemplateView):
    template_name = 'accounts/cancelled.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Six week Weight loss',
                        'quantity': 1,
                        'currency': 'inr',
                        'amount': '100000',
                    },
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})



