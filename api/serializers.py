# from re import search
# from django.db.models import fields
from rest_framework import serializers
# from rest_framework.utils import field_mapping
from .models import Room, HouseRule, Amenitie, Location


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'owner',
            'property_id',
            'category_type',
            'images',
            'photo',
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
            'deposit',
            'single_occupancy',
            'preferred_gender'
        )


class AmenitieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amenitie
        fields = (
            'amenty_id',
            'min_stay',
            'max_stay',
            'is_furnished',
            'has_kitchen',
            'has_internet',
            'has_parking',
            'has_garden',
            'has_terrace',
            'total_bedrooms',
            'available_from',
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
