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
<<<<<<< HEAD
        fields = ['id', 'title', 'location', 'contact', 'owner' ,'image', 'price','property_type']
=======
        fields = ['id', 'title', 'location', 'contact', 'owner', 'image']

>>>>>>> c12415305d1be4ff6baec1dd1c20526c2c68b374

class PropertyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
<<<<<<< HEAD
        fields = ['title']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'agent', 'customer_name', 'comment_text', 'created_at']

class AgentRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
=======
        fields = ['title']
>>>>>>> c12415305d1be4ff6baec1dd1c20526c2c68b374
