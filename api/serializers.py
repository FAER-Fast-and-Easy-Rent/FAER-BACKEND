from rest_framework import serializers
from .models import Media, Room


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'file_name',
            'url',
            'mime_type',
            'content_object'

        )


class RoomSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=500)
    home_type = serializers.CharField()
    room_type = serializers.CharField()
    total_occupancy = serializers.IntegerField()
    total_bedrooms = serializers.IntegerField()
    total_bathrooms = serializers.IntegerField()
    is_furnished = serializers.BooleanField()
    has_kitchen = serializers.BooleanField()
    address = serializers.CharField()
    images = serializers.ImageField(max_length=None)

    class Meta:
        model = Room
        fields = (
            'title',
            'price',
            'description',
            'home_type',
            'room_type',
            'total_occupancy',
            'total_bedrooms',
            'total_bathrooms',
            'is_furnished',
            'has_kitchen',
            'address',
            'images'
        )
