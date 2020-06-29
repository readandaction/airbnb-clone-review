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
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_USA = "usa"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Kr"),
        (LANGUAGE_USA, "USA"),
    )

    CURRENCY_KR = "kr"
    CURRENCY_USA = "usa"
    CURRENCY_CHOICES = (
        (CURRENCY_KR, "Kr"),
        (CURRENCY_USA, "USA"),
    )
    avatar = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(blank=True, max_length=40, choices=GENDER_CHOICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, blank=True)
    superhost = models.BooleanField(default=False)

