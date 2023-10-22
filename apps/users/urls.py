from django.urls import path, include
from apps.users.views import RegisterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"signup", RegisterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]