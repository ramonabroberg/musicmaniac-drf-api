from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'The image size is larger than 2 MB'
            )
        if value.image.width > 4000:
            raise serializers.ValidationError(
                'The image width is larger than 4000px'
            )
        if value.image.height > 4000:
            raise serializers.ValidationError(
                'The image height is larger than 4000px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'band', 'title', 'image', 'instrument', 'genre',
            'city', 'website', 'description', 'created_at', 'is_owner'
        ]