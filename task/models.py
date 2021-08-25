from django.db import models

class AlgorithmModel(models.Model):
    text = models.TextField()
    label = models.TextField()
