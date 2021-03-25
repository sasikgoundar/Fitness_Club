from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms

# Create your models here

class Fitness(models.Model):
    fitness_type = models.CharField(max_length=50, null=True)
    fitness_desc = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.fitness_type

class Trainer(models.Model):
    GENDER = (
        ('M','Male'),
        ('F','Female'),
    )
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    fitness = models.ManyToManyField(Fitness)
    email_id = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1,choices=GENDER, null=True)
    dob = models.DateField(null=True)
    phone_no = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.first_name


class Plan(models.Model):
    name = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(max_length=10, null=True)
    duration = models.DurationField()

    def __str__(self):
        return self.name
class Member(models.Model):
    GENDER = (
        ('M','Male'),
        ('F','Female'),
    )
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, null=True, on_delete=models.SET_NULL)
    fitness = models.ManyToManyField(Fitness)
    username = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email_id = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1,choices=GENDER, null=True)
    dob = models.DateField(null=True)
    phone_no = models.CharField(max_length=50, null=True)
    alt_phone_no = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    plan = models.ForeignKey(Plan, null=True, on_delete=models.SET_NULL)
    join_date = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.user

"""@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.member.save()"""


