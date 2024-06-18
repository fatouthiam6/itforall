from django.db import models


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    code = models.TextField(null=True)
    instructions = models.TextField(null=True)
