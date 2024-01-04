from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

INSTRUMENT_CHOICES = [
    ('select_instrument', 'Please select an instrument'),
    ('vocalist_wanted', 'Vocalist wanted'),
    ('vocalist_here', 'Vocalist here'),
    ('guitarist_wanted', 'Guitarist wanted'),
    ('guitarist_here', 'Guitarist here'),
    ('bassist_wanted', 'Bassist wanted'),
    ('bassist_here', 'Bassist here'),
    ('keyboardist_wanted', 'Keyboardist wanted'),
    ('keyboardist_here', 'Keyboardist here'),
    ('drummer_wanted', 'Drummer wanted'),
    ('drummer_here', 'Drummer here'),
    ('other', 'Other'),
]

GENRE_CHOICES = [
    ('select_genre', 'Please select a genre'),
    ('rock', 'Rock'),
    ('metal', 'Metal'),
    ('pop', 'Pop'),
    ('country', 'Country'),
    ('jazz', 'Jazz'),
    ('folk', 'Folk'),
    ('electronic_dance_music', 'Electronic Dance Music'),
    ('r&b', 'R&B'),
    ('classical', 'Classical'),
    ('other', 'Other'),
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
