from django.db import models


class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)


class Workout(models.Model):
    date_time = models.DateTimeField()
    workout_name = models.CharField(max_length 60)

class Exercise(models.Model):
    exercise_id = models.IntegerField()
