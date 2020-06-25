from rest_framework.serializers import ModelSerializer
from api.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ['secret_key']
