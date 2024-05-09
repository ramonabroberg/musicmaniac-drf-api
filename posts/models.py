from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

INSTRUMENT_CHOICES = [
    ('select_instrument', 'Select instrument...'),
    ('bassist_here', 'Bassist here'),
    ('bassist_wanted', 'Bassist wanted'),
    ('drummer_here', 'Drummer here'),
    ('drummer_wanted', 'Drummer wanted'),
    ('guitarist_here', 'Guitarist here'),
    ('guitarist_wanted', 'Guitarist wanted'),
    ('keyboardist_here', 'Keyboardist/pianist here'),
    ('keyboardist_wanted', 'Keyboardist/pianist wanted'),
    ('vocalist_here', 'Vocalist here'),
    ('vocalist_wanted', 'Vocalist wanted'),
    ('other', 'Other'),
]

GENRE_CHOICES = [
    ('select_genre', 'Select genre...'),
    ('blues', 'Blues'),
    ('classical', 'Classical'),
    ('country', 'Country'),
    ('electronic_dance_music', 'Electronic Dance Music'),
    ('folk', 'Folk'),
    ('jazz', 'Jazz'),
    ('metal', 'Metal'),
    ('pop', 'Pop'),
    ('r&b', 'R&B'),
    ('rock', 'Rock'),
    ('soul', 'Soul'),
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
