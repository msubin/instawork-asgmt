from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


# Create your models here.
class Members(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isAdmin = models.BooleanField()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    email = models.EmailField()

    def add_member(self):
        pass

    def edit_member(self):
        pass

    def delete_member(self):
        pass

    def __str__(self):
        return self.name
