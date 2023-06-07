from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from djoser.views import UserViewSet as DjoserUserViewSet
from .serializers import UserCreateSerializer
from .models import Agent, Property
from .serializers import PropertySerializer

class UserViewSet(DjoserUserViewSet):
    queryset = Agent.objects.all()
    serializer_class = UserCreateSerializer

class CreatePropertyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePropertyView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
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

class DeletePropertyView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if property.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]



