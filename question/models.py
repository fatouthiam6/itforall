from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)
    image_path = models.TextField(null=True)
