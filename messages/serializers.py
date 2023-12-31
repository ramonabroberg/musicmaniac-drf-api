from rest_framework import serializers
from django.contrib.auth.models import User
from messages.models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'sent_at']