from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer
from posts.serializers import InstrumentSerializer, GenreSerializer
from posts.models import Post, INSTRUMENT_CHOICES, GENRE_CHOICES


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        interested_count=Count('interested', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        'instrument': ['exact'],
        'genre': ['exact'],
    }
    search_fields = [
        'owner__username',
        'title',
        'instrument',
        'genre',
        'city',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        instrument = self.request.query_params.get('instrument')
        genre = self.request.query_params.get('genre')

        if instrument and not genre:
            queryset = queryset.filter(instrument=instrument)
        elif genre and not instrument:
            queryset = queryset.filter(genre=genre)
        elif instrument and genre:
            queryset = queryset.filter(instrument=instrument, genre=genre)
        
        return queryset


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostInformation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        interested_count=Count('interested', distinct=True),
        comments_count=Count('comment', distinct=True)
    )


class InstrumentChoice(generics.ListAPIView):
    serializer_class = InstrumentSerializer

    def get_queryset(self):
        return (
            [{'id': value[0], 'name': value[1]} for value in INSTRUMENT_CHOICES]
        )


class GenreChoice(generics.ListAPIView):
    serializer_class = GenreSerializer

    def get_queryset(self):
        return (
            [{'id': value[0], 'name': value[1]} for value in GENRE_CHOICES]
        )