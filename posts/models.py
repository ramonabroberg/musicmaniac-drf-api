from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

INSTRUMENT_CHOICES = [
    ('Select_instrument', 'Select instrument...'),
    ('Bassist_here', 'Bassist here'),
    ('Bassist_wanted', 'Bassist wanted'),
    ('Drummer_here', 'Drummer here'),
    ('Drummer_wanted', 'Drummer wanted'),
    ('Guitarist_here', 'Guitarist here'),
    ('Guitarist_wanted', 'Guitarist wanted'),
    ('Keyboardist_here', 'Keyboardist/pianist here'),
    ('Keyboardist_wanted', 'Keyboardist/pianist wanted'),
    ('Vocalist_here', 'Vocalist here'),
    ('Vocalist_wanted', 'Vocalist wanted'),
    ('Other', 'Other'),
]

GENRE_CHOICES = [
    ('Select_genre', 'Select genre...'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic_dance_music', 'Electronic Dance Music'),
    ('Folk', 'Folk'),
    ('Jazz', 'Jazz'),
    ('Metal', 'Metal'),
    ('Pop', 'Pop'),
    ('R&B', 'R&B'),
    ('Rock', 'Rock'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    instrument = models.CharField(choices=INSTRUMENT_CHOICES, max_length=30)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=30)
    city = models.CharField(blank=True, max_length=100)
    website = models.URLField(blank=True, max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
