from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from interested.models import Interested
from interested.serializers import InterestedSerializer


class InterestedList(generics.ListCreateAPIView):
    serializer_class = InterestedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Interested.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InterestedInformation(generics.RetrieveDestroyAPIView):
    serializer_class = InterestedSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Interested.objects.all()
