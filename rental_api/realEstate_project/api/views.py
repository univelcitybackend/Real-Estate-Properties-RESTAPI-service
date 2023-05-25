from django.shortcuts import render

# Create your views here.
from djoser.views import UserViewSet as DjoserUserViewSet
from .serializers import UserCreateSerializer
from .models import Agent

class UserViewSet(DjoserUserViewSet):
    queryset = Agent.objects.all()
    serializer_class = UserCreateSerializer