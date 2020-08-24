# Generated by Django 2.1.7 on 2020-07-09 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='slug',
            field=models.SlugField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='slug',
            field=models.SlugField(default='qwerty', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]