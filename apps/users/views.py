from rest_framework.permissions import AllowAny
from rest_framework import mixins, viewsets, status
from django.contrib.auth import get_user_model

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from apps.users.serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.settings import api_settings

from social_network.services import update_login_history



class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER

    def post(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        else:
            update_login_history(request.data.get('username'), True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

