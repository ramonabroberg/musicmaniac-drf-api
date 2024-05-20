from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages'
    )
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sent_at']
    
    def __str__(self):
        return f'{self.sent_at} {self.sender} - {self.receiver}'
