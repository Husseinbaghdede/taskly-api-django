from django.contrib.auth.models import User

from rest_framework import viewsets,mixins
from .serializers import UserSerializer,ProfileSerializer
from .models import Profile
from .permissions import isUserOwnerOrGetAndPostOnly,isProfileOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [isUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    permission_classes = [isProfileOwnerOrReadOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer