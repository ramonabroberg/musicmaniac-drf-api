from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from interested.models import Interested
from interested.serializers import InterestedSerializer


class InterestedList(generics.ListCreateAPIView):
    """
    Shows interests and is possible to show your interest of a post
    by clicking on the star icon while logged in.
    """
    serializer_class = InterestedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Interested.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InterestedInformation(generics.RetrieveDestroyAPIView):
    """
    Show interest on a post or take it back,
    all while logged in.
    """
    serializer_class = InterestedSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Interested.objects.all()
