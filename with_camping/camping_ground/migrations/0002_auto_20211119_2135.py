# Generated by Django 3.2.5 on 2021-11-19 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camping_ground', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campingground',
            name='desc_img',
            field=models.ImageField(default='static/lantern.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='campingground',
            name='price',
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name='campingground',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]