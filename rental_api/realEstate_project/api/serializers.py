from djoser.serializers import UserSerializer,UserCreateSerializer
from .models import Agent


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Agent
        fields = ['username', 'first_name', 'last_name','email']


class UserSerializer(UserSerializer):
    class Meta(UserSerializer):
        model=Agent
        fields = ['id', 'email', 'username', 'first_name', 'last_name']