# Generated by Django 3.0.6 on 2020-07-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0005_auto_20200716_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='user',
        ),
        migrations.AlterField(
            model_name='workout',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
