from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer
from posts.serializers import InstrumentSerializer, GenreSerializer
from posts.models import Post, INSTRUMENT_CHOICES, GENRE_CHOICES


class PostList(generics.ListCreateAPIView):
    """
    See posts or upload posts while logged in.
    Search fields to filter the posts by different values.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        interested_count=Count('interested', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'instrument',
        'genre',
        'city',
        'description',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostInformation(generics.RetrieveUpdateDestroyAPIView):
    """
    See posts and if the user owns it, they can edit/delete it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        interested_count=Count('interested', distinct=True),
        comments_count=Count('comment', distinct=True)
    )


class Instruments(generics.ListAPIView):
    """
    See intruments available.
    """
    serializer_class = InstrumentSerializer

    def get_queryset(self):
        return (
            [{"id": value[0], "name": value[1]} for value in INSTRUMENT_CHOICES]
        )


class Genres(generics.ListAPIView):
    """
    See genres available.
    """
    serializer_class = GenreSerializer

    def get_queryset(self):
        return (
            [{"id": value[0], "name": value[1]} for value in GENRE_CHOICES]
        )
