from .models import Media, Room, Vehicle
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'file_name',
            'url',
            'mime_type',
            'content_object'

        )


class MediaObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `content_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        if isinstance(value, Room):
            return 'Room: ' + value.images
        elif isinstance(value, Vehicle):
            return 'Vehicle: ' + value.images
        raise Exception('Unexpected type of tagged object')


class RoomSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=Room.objects.all())])
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


class VehicleSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=500)
    capacity = serializers.IntegerField()
    vehicle_type = serializers.CharField()
    brand = serializers.CharField()
    model = serializers.CharField()
    images = serializers.ImageField(max_length=None)
    # images = MediaObjectRelatedField(many=True,read_only=True)

    class Meta:
        model = Vehicle
        fields = (
            'name',
            'price',
            'description',
            'capacity',
            'vehicle_type',
            'brand',
            'model',
            'images'
        )

# class ReservationSerializer(serializers.ModelSerializer):
