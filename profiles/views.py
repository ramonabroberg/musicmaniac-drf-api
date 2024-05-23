from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from profiles.serializers import ProfileSerializer
from profiles.models import Profile


class ProfileList(generics.ListAPIView):
    """
    See profiles.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-created_at')


class ProfileInformation(generics.RetrieveUpdateAPIView):
    """
    See more information of the profiles.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all().order_by('-created_at')
