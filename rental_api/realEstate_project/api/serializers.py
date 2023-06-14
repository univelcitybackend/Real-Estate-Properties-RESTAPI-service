from rest_framework import serializers
from djoser.serializers import UserSerializer,UserCreateSerializer
from .models import Agent,Property, Comment


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Agent
        fields = ['username', 'first_name', 'last_name','email']

class AgentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['first_name','last_name']

class AgentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Agent
        fields = ['id','username' , 'first_name','last_name', 'email']

class UserSerializer(UserSerializer):
    class Meta(UserSerializer):
        model=Agent
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
<<<<<<< HEAD
        fields = ['id', 'title', 'location', 'contact', 'owner' ,'image', 'price','property_type']

class PropertyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'agent', 'customer_name', 'comment_text', 'created_at']
=======
        fields = ['id', 'title', 'address', 'contact', 'owner', 'image']
>>>>>>> akin
