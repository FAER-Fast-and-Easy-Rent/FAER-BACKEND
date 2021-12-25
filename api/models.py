from django.db import models

# Create your models here.


class Amenitie(models.Model):
    amenty_id = models.AutoField(primary_key=True)
    is_furnished = models.BooleanField()
    has_parking = models.BooleanField()
    has_garden = models.BooleanField()
    has_terrace = models.BooleanField()
    has_attach_bathrooms = models.BooleanField()
    floor_no = models.IntegerField()
    total_rooms_in_house = models.IntegerField()

    def __str__(self):
        return str(self.amenty_id)


class HouseRule(models.Model):
    gender_pref = (
        ("M", "MALE"),
        ("F", "FEMALE"),
        ("B", "BOTH")
    )
    rule_id = models.AutoField(primary_key=True)
    smoking_allowed = models.BooleanField()
    pets_allowed = models.BooleanField()
    couples_allowed = models.BooleanField()
    preferred_gender = models.CharField(max_length=1, choices=gender_pref)

    def __str__(self):
        return str(self.rule_id)


class Location(models.Model):
    states = (
        ("1", "STATE 1"),
        ("2", "STATE 2"),
        ("3", "STATE 3"),
        ("4", "STATE 4"),
        ("5", "STATE 5"),
        ("6", "STATE 6"),
        ("7", "STATE 7"),
    )
    location_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=5)
    state = models.CharField(max_length=1, choices=states)

    def __str__(self):
        return str(self.location_id)


class Room(models.Model):
    category_types = (
        ("R", "ROOM"),
        ("F", "FLAT"),
        ("A", "APPARTMENT"),
        ("H", "HOUSE")
    )
    property_id = models.AutoField(primary_key=True)
    category_type = models.CharField(max_length=1, choices=category_types)
    images = models.URLField(max_length=200)
    no_of_room_to_rent = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    amenities = models.ForeignKey(to='Amenitie', on_delete=models.CASCADE)
    house_rule = models.ForeignKey(to='HouseRule', on_delete=models.CASCADE)
    location = models.ForeignKey(to='Location', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.property_id)
