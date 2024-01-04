from rest_framework import generics, permissions
from django.db.models import Q
from messaging.models import Message
from messaging.serializers import MessageSerializer
from posts.models import Post


class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        conversations = Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        )

        distinct_users = set()
        unique_conversations = []
        for conversation in conversations:
            if conversation.receiver not in distinct_users:
                distinct_users.add(conversation.receiver)
                unique_conversations.append(conversation)

        return unique_conversations

    def perform_create(self, serializer):
        serializer.save(
            sender=self.request.user,
            receiver=serializer.validated_data['receiver']
        )


class MessageConversation(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        other_user_id = self.kwargs['user_id']
        return Message.objects.filter(
            (Q(sender=user,
               receiver_id=other_user_id) | Q(sender_id=other_user_id,
                                              receiver=user))
        )


class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post_id')
        post_user = Post.objects.get(pk=post_id).user
        serializer.save(sender=self.request.user, receiver=post_user)
