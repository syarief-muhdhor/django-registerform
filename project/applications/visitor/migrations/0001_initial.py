# Generated by Django 3.2.7 on 2021-09-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile_number', models.CharField(max_length=25, verbose_name='Mobile Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date Of Birth')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True, verbose_name='Gender')),
            ],
            options={
                'unique_together': {('mobile_number', 'email')},
            },
        ),
    ]
