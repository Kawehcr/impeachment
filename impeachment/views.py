from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImpeachmentSerializers
from .models import Impeachment

class RequestTestAPI(APIView):

    def get(self, request, format=None):
        return Response({"API": "OK"})

class ImpeachmentCreateViewSet(generics.CreateAPIView):

    queryset = Impeachment.objects.all()
    serializer_class = ImpeachmentSerializers

class ImpeachmentRetrieveUpdateDeleteViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = Impeachment.objects.all()
    serializer_class = ImpeachmentSerializers

class ImpeachmentListViewSet(generics.ListAPIView):

    queryset = Impeachment.objects.all()
    serializer_class = ImpeachmentSerializers