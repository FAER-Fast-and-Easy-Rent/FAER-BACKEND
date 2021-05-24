from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RoomSerializer, AmenitieSerializer, HouseRuleSerializer, LocationSerializer
from .models import Room, Amenitie, HouseRule, Location

# Create your views here.

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class AmentieViewSet(viewsets.ModelViewSet):
    queryset = Amenitie.objects.all()
    serializer_class = AmenitieSerializer

class HouseRuleViewSet(viewsets.ModelViewSet):
    queryset = HouseRule.objects.all()
    serializer_class = HouseRuleSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


