from django.urls import include, path
from rest_framework.routers import SimpleRouter
from apps.posts.views import PostListViewSet, PostViewSet, PostLikeApiView, AnaliticsPostViewSet


router = SimpleRouter()
router.register(r"posts-list", PostListViewSet)
router.register(r"posts", PostViewSet)
router.register(r"analitics", AnaliticsPostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("like/<int:pk>/", PostLikeApiView.as_view(), name='post-like'),
]
