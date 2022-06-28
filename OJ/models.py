from django.db import models

# Create your models here.

class Problems(models.Model):
    statement = models.CharField(max_length=1200)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=1200)
    difficulty = models.CharField(max_length=10)

class Solutions(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=200)
    submitted_at = models.DateTimeField('date submitted')

class TestCases(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
