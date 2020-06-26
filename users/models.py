from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ User Model Definition """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    description = models.TextField(blank=True)
    gender = models.CharField(blank=True, max_length=40, choices=GENDER_CHOICES)

