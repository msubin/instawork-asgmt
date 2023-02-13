from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    isAdmin = models.BooleanField(default=False)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True)
    email = models.EmailField(null=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
