from rest_framework import serializers
from djoser.serializers import UserSerializer,UserCreateSerializer
from .models import Agent,Property


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Agent
        fields = ['username', 'first_name', 'last_name','email']


class UserSerializer(UserSerializer):
    class Meta(UserSerializer):
        model=Agent
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class AgentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class AgentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'location', 'contact', 'owner', 'image']


class PropertyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title']