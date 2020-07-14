from django.db import models


class MuscleGroup(models.Model):
    name = models.CharField(max_length=200)
    api_id = models.IntegerField()
    


    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name