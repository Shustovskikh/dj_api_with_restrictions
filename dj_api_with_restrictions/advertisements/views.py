from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer, UserSerializer
from advertisements.filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class UserViewSet(ModelViewSet):
    """ViewSet для пользователей."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["update", "partial_update"]:
            return [IsAuthenticated()]
        return []