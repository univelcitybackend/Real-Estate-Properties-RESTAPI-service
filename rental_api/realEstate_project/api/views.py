from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from djoser.views import UserViewSet as DjoserUserViewSet
from .serializers import UserCreateSerializer
from .models import Agent, Property
from .serializers import PropertySerializer

class UserViewSet(DjoserUserViewSet):
    queryset = Agent.objects.all()
    serializer_class = UserCreateSerializer

@api_view(['POST'])
def create_property(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_property(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if property.owner != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = PropertySerializer(property, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_property(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if property.owner != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    property.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)