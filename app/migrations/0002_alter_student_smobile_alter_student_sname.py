# Generated by Django 4.2.7 on 2024-01-11 15:33

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Smobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('[6-9]\\d{9}')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='Sname',
            field=models.CharField(max_length=20, validators=[app.models.letter]),
        ),
    ]