from datetime import datetime
from rest_framework import viewsets, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer, AnaliticsSerializer, LikePostSerializer
from rest_framework.permissions import IsAuthenticated
from apps.posts.permissions import IsAuthorOrReadOnly
from dj_rql.drf.backend import RQLFilterBackend
from .filters import PostsFilters
from django.db.models import Count
from django.db.models.functions import TruncDate


class PostListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    rql_filter_class = PostsFilters
    filter_backends = (RQLFilterBackend,)
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeApiView(APIView):
    serializer_class = LikePostSerializer
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


class AnaliticsPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = AnaliticsSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        start_date = datetime.strptime(self.request.GET.get('date_from'), '%Y-%m-%d').date()
        end_date = datetime.strptime(self.request.GET.get('date_to'), '%Y-%m-%d').date()
        return Post.objects.filter(created_at__range=(start_date, end_date)).annotate(day=TruncDate('created_at')).\
            values('day').annotate(count=Count('id'))
