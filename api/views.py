# from django.shortcuts import render
from .models import Room
from .producer import publish
from .utils import write_to_tmp
from .serializers import RoomSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.parsers import FormParser, MultiPartParser


class IsAuthenticatedOrReadOnly(BasePermission):

    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if (request.method in SAFE_METHODS or
            request.user and
                request.user.is_authenticated):
            return True
        return False


class RoomViewSet(viewsets.ViewSet):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            data['images'] = write_to_tmp(file=request.FILES['images'])
            data['user'] = request.user.email
            publish(method="create_room", body=data)
            return Response({'mesage': 'Welcome to post', 'data': data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'mesage': 'success'})
