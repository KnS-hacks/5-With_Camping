# Generated by Django 3.2.5 on 2021-11-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camping_ground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campingground',
            name='desc_img',
            field=models.FileField(blank=True, null=True, upload_to='desc_img'),
        ),
    ]
