# Generated by Django 2.2 on 2020-08-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0017_auto_20200810_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
