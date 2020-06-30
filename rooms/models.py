from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models


class AbstractItem(core_models.TimeStampedModel):
    """ AbstractItem Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
        users_models.User, related_name="room", on_delete=models.CASCADE, null=True
    )
    room_types = models.ForeignKey(
        RoomType, related_name="room", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(Amenity, related_name="room", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="room", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="room", blank=True)

    def __str__(self):
        return self.name
