from rest_framework import permissions
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from apps.users.views import TokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Social Network API",
      default_version='v1',
      description="Documentation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include('apps.users.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('apps.posts.urls')),
    path('api/v1/', include('rest_framework.urls')),
]

