# Generated by Django 3.1.5 on 2021-03-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_member_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='alt_phone_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]