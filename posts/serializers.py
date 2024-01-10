from rest_framework import serializers
from posts.models import Post
from interested.models import Interested


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    interested_id = serializers.SerializerMethodField()
    interested_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if hasattr(value, 'image') and value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'The image size is larger than 2 MB'
            )
        if hasattr(value, 'image') and value.image.width > 4000:
            raise serializers.ValidationError(
                'The image width is larger than 4000px'
            )
        if hasattr(value, 'image') and value.image.height > 4000:
            raise serializers.ValidationError(
                'The image height is larger than 4000px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_interested_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            interested = Interested.objects.filter(
                owner=user, post=obj
            ).first()
            return interested.id if interested else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'image', 'instrument', 'genre',
            'city', 'website', 'description', 'created_at', 'is_owner',
            'profile_id', 'profile_image', 'interested_id', 'interested_count'
        ]


class InstrumentSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()


class GenreSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
