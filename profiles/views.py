from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from profiles.serializers import ProfileSerializer
from profiles.models import Profile


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileInformation(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()