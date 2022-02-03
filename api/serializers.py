from .models import Media, Room, Vehicle
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.serializers import UserSerializer


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'file_name',
            'url',
            'mime_type'
        )


class MediaObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `content_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize.
        """
        serializer = MediaSerializer(value)

        return serializer.data


class RoomSerializer(serializers.HyperlinkedModelSerializer):
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
    image = serializers.ImageField(max_length=None, write_only=True)

    images = MediaObjectRelatedField(read_only=True, many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        depth = 1
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
            'images',
            'owner',
            'image'
        )
        read_only_fields = ('images', 'owner')


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=500)
    capacity = serializers.IntegerField()
    vehicle_type = serializers.CharField()
    brand = serializers.CharField()
    model = serializers.CharField()
    image = serializers.ImageField(max_length=None, write_only=True)

    images = MediaObjectRelatedField(read_only=True, many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        depth = 1
        model = Vehicle
        fields = (
            'name',
            'price',
            'description',
            'capacity',
            'vehicle_type',
            'brand',
            'model',
            'images',
            'owner',
            'image'
        )
        read_only_fields = ('images', 'owner')

# class ReservationSerializer(serializers.ModelSerializer):
