# Generated by Django 3.2.5 on 2021-11-19 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camping_ground', '0002_auto_20211119_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campingground',
            name='desc_img',
        ),
    ]