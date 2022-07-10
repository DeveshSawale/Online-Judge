

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Problem(models.Model):
    statement = models.CharField(max_length=1200)
    name = models.CharField(max_length=200)
    output = models.FileField(max_length=1000,default='/Devesh/acc_out.txt',upload_to='Devesh')
    difficulty = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Solution(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default = 1)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length = 10)
    verdict = models.CharField(max_length=200)
    submitted_at = models.DateTimeField('date submitted')
    submitted_code = models.CharField(max_length=250)

    def __str__(self):
        return self.verdict


class TestCases(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return self.input