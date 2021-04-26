# Generated by Django 3.1.5 on 2021-02-20 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_member_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email_id', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('dob', models.DateField(null=True)),
                ('phone_no', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.trainer'),
        ),
    ]