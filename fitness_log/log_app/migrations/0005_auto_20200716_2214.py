# Generated by Django 3.0.6 on 2020-07-17 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log_app', '0004_auto_20200716_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='reps',
            new_name='set1_reps',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='weight_lifted',
            new_name='set1_weight_lifted',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='sets',
            new_name='set2_reps',
        ),
        migrations.AddField(
            model_name='exercise',
            name='set2_weight_lifted',
            field=models.CharField(default='10 lbs', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='set3_reps',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='set3_weight_lifted',
            field=models.CharField(default='10 lbs', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='set4_reps',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='set4_weight_lifted',
            field=models.CharField(default='10 lbs', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='log_app.Workout'),
        ),
    ]
