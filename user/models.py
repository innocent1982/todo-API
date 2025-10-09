from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    regex = "^(\+265\d{9}|0\d{9})$"
    phone = models.CharField(validators=[RegexValidator(regex=regex), MinLengthValidator(10)], unique=True, max_length=13, null=False, blank=False) 
    age = models.IntegerField(null=False, blank=False)

    def save(self, *args, **kwargs):
        password = self.password
        self.set_password(password)
        super().save(*args, **kwargs)

