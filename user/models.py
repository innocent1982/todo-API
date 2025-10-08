from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    regex = "^(\+265\d{9}|0\d{9})$"
    phone = models.CharField(validators=[RegexValidator(regex=regex), MinLengthValidator(10)], unique=True, max_length=13, null=False, blank=False) 
    age = models.IntegerField(null=False, blank=False)

    objects = UserManager()

