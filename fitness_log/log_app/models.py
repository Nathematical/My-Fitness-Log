from django.db import models


class Workout(models.Model):
    date_created = models.DateTimeField()
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name

        
class Exercise(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight_lifted = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return self.name

