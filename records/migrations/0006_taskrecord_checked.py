# Generated by Django 2.2 on 2020-07-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskrecord',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
