# Generated by Django 3.1.5 on 2021-02-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_fitness'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='fitness',
            field=models.ManyToManyField(to='accounts.Fitness'),
        ),
    ]