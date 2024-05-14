from rest_framework import serializers
from messaging.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'sent_at']
        read_only_fields = ['sender']
