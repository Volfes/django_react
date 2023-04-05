from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

def main(request):
    return HttpResponse('Hi')


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer