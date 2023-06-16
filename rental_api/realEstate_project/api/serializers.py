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
        fields = ['id', 'title', 'location', 'contact', 'owner' ,'image', 'price','property_type']
<<<<<<< HEAD

=======
>>>>>>> 7bd0d1c5732176b0daab09b212f68e930a7af6c3

class PropertyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title']

class CommentSerializer(serializers.ModelSerializer):
    agent_id= serializers.ReadOnlyField()
    class Meta:
        model = Comment
        fields = ['id', 'agent_id', 'customer_name', 'comment_text', 'created_at']

class AgentRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
<<<<<<< HEAD
    fields = ['title']
=======
        fields = ['title']

>>>>>>> 7bd0d1c5732176b0daab09b212f68e930a7af6c3
