from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from accounts.serializer import UserSerializer, UserProfileSerializer


class BaseUserViewMixin:
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()


class BaseUserProfileViewMixin:
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]