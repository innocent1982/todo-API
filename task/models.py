from django.db import models
from user.models import User

class Task(models.Model):
    choices = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low")
    ]
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.CharField(max_length=200)
    priority = models.CharField(choices=choices, default="low")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def save(self, *args, **kwargs):
        start = self.start_time
        end = self.end_time
        duration = end - start
        print(duration)
        self.duration = str(duration)
        super().save(*args, **kwargs)
