from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-picture_xzjf4x')
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(default=datetime(2023, 12, 22))

    class Meta:
        ordering: ['-created_at']
    
    def __str__(self):
        return f"{self.user}'s profile"


def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)