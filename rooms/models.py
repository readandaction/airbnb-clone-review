from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=130)
    description = models.TextField(blank=True)
    country = CountryField()
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=140)
    price = models.IntegerField()
    guests = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    bedrooms = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField()
    host = models.ForeignKey(
        users_models.User, related_name="room", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
