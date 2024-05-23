from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Interested(models.Model):
    """
    Interested model, related to user and post.
    It's not possible for a user to like a post more than once
    because of unique_together.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='interested'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} - {self.post}'
