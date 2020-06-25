from api.models import Post
from api.serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class PostsViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk='id'):
        post = self.get_object()
        post.upvotes += 1
        post.save()
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data)

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk='id'):
        post = self.get_object()
        post.downvotes += 1
        post.save()
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data)
