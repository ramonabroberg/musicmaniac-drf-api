from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer
from posts.models import Post

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        interested_count=Count('interested', distinct=True)
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
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostInformation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        interested_count=Count('interested', distinct=True)
    )