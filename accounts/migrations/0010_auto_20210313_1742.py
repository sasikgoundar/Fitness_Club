# Generated by Django 3.1.5 on 2021-03-13 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210313_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('amount', models.CharField(max_length=10, null=True)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.plan'),
        ),
    ]