# Generated by Django 3.1.5 on 2021-03-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210226_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('amount', models.CharField(max_length=10, null=True)),
                ('duration', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='plan',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='fitness',
            field=models.ManyToManyField(to='accounts.Fitness'),
        ),
    ]