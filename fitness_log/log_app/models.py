from django.db import models
from log_users.models import User


class Workout(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Exercise(models.Model):
    # category = models.CharField(max_length=200)
    category = models.IntegerField()
    name = models.CharField(max_length=200)
    set1_reps = models.IntegerField()
    set2_reps = models.IntegerField()
    set3_reps = models.IntegerField()
    set4_reps = models.IntegerField()
    set1_weight_lifted = models.CharField(max_length=200)
    set2_weight_lifted = models.CharField(max_length=200)
    set3_weight_lifted = models.CharField(max_length=200)
    set4_weight_lifted = models.CharField(max_length=200)
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT, related_name='exercises')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='exercises')

    def __str__(self):
        return self.name

