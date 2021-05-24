from re import search
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Room, HouseRule, Amenitie, Location

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = (
            'property_id',
            'category_type',
            'images',
            'no_of_room_to_rent',
            'price',
            'description',
            'amenities',
            'house_rule',
            'location'
        )

class HouseRuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HouseRule
        fields = (
            'rule_id',
            'smoking_allowed',
            'pets_allowed',
            'couples_allowed',
            'preferred_gender'
        )

class AmenitieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amenitie
        fields = (
            'amenty_id',
            'is_furnished',
            'has_parking',
            'has_garden',
            'has_terrace',
            'has_attach_bathrooms',
            'floor_no',
            'total_rooms_in_house'
        )

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            'location_id',
            'street_address',
            'city',
            'postal_code',
            'state'
        )