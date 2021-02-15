from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class List(models.Model):
    task = models.CharField(max_length=256)
    #dateCreated = models.DateTimeField(default=timezone.now)
    #    0 = No, 1 = daily, 2 = weekly, 3 = monthly
    #repeating = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
