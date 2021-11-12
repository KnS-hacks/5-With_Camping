# Generated by Django 3.2.5 on 2021-11-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camping_tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campingtools',
            name='category',
            field=models.CharField(choices=[('tent', 'tent'), ('grill', 'grill'), ('table', 'table'), ('lantern', 'lantern'), ('firewood', 'firewood')], default='tent', max_length=20),
        ),
        migrations.AddField(
            model_name='campingtools',
            name='image',
            field=models.ImageField(default='static/lantern.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='campingtools',
            name='rental_fee',
            field=models.IntegerField(default=20000),
        ),
        migrations.AlterField(
            model_name='campingtools',
            name='quantity',
            field=models.IntegerField(default=10),
        ),
    ]