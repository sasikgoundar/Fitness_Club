from django.db import models


# Create your models here

class Trainer(models.Model):
    GENDER = (
        ('M','Male'),
        ('F','Female'),
    )
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email_id = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1,choices=GENDER, null=True)
    dob = models.DateField(null=True)
    phone_no = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.first_name

class Fitness(models.Model):
    fitness_type = models.CharField(max_length=50, null=True)
    fitness_desc = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.fitness_type


class Member(models.Model):
    GENDER = (
        ('M','Male'),
        ('F','Female'),
    )
    trainer = models.ForeignKey(Trainer, null=True, on_delete=models.SET_NULL)
    fitness = models.ManyToManyField(Fitness)
    username = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email_id = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1,choices=GENDER, null=True)
    dob = models.DateField(null=True)
    phone_no = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    join_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name



