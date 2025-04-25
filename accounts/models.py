from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    username_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9@.+-_ ]+$',  # Allow spaces in addition to default characters
        message="Username can only contain letters, numbers, spaces, and @/./+/-/_ characters."
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Add this line
    address = models.TextField(blank=True, null=True)