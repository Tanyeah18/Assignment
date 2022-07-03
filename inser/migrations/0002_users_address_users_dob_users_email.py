# Generated by Django 4.0.5 on 2022-07-03 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.TextField(blank=b'I01\n'),
        ),
        migrations.AddField(
            model_name='users',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(blank=b'I01\n', max_length=30),
        ),
    ]
