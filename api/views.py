# from django.shortcuts import render
from .models import Room
from .serializers import RoomSerializer,TestSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.core.serializers import serialize, deserialize
from rest_framework.parsers import FormParser,MultiPartParser

from multiprocessing import Pool,cpu_count
from .producer import publish
from .utils import write_to_tmp

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
            return Response({'mesage':'Welcome to post','data':data})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        return Response({'mesage':'success'})

class TestViewSet(viewsets.ViewSet):

    parser_classes = (FormParser, MultiPartParser)
    serializer_class = TestSerializer
    def list(self, request):
        # queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        return Response({'mesage':'success'})

    def create(self, request):
        serializer = TestSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            data['image'] = write_to_tmp(file=request.FILES['image'])
            publish(method="create_product", body=data)
            return Response({'mesage':'Welcome to post','data':data})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        