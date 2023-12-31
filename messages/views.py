from rest_framework import generics, permissions
from django.contrib.auth.models import User
from messages.models import Message
from messages.serializers import UserSerializer, MessageSerializer

class MesssageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user)
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageConversation(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        other_user_id = self.kwargs['user_id']
        return Message.objects.filter(
            (models.Q(sender=user, receiver_id=other_user_id) | models.Q(
                sender_id=other_user_id, receiver=user))
        )