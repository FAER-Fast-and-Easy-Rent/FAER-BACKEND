# from django.shortcuts import render
from .models import Room
from .producer import publish
from .utils import write_to_tmp
from .serializers import RoomSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser


class RoomViewSet(viewsets.ViewSet):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = RoomSerializer

    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            data['images'] = write_to_tmp(file=request.FILES['images'])
            publish(method="create_room", body=data)
            return Response({'mesage': 'Welcome to post', 'data': data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'mesage': 'success'})
