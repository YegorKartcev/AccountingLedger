# Generated by Django 2.2 on 2020-07-16 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0010_auto_20200716_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('checked', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskRecords', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='content',
        ),
        migrations.DeleteModel(
            name='TaskRecord',
        ),
        migrations.AddField(
            model_name='choice',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Task'),
        ),
    ]
