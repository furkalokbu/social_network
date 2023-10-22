from rest_framework import viewsets, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from apps.posts.permissions import IsAuthorOrReadOnly


class PostListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated ,IsAuthorOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeApiView(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk):
        return get_object_or_404(Post, pk=pk)
        
     
    def get(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)
        post.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
