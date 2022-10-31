from django.db import models

# Create your models here.
import random

max_length = 200
class HngUserModel(models.Model):

    first_name = models.CharField(max_length=max_length, null=False, blank=False)
    last_name = models.CharField(max_length=max_length, null=False, blank=False)
    email = models.EmailField(max_length=max_length, null=False, blank=False, unique=True)
    stack = models.TextField()
    date_joined = models.DateField()

    def nickname(self):
        return f"{self.first_name}" + random.randint(3, 10)
