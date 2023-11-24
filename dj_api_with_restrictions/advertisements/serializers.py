from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement

class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)

class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, attrs):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context['request'].user
        if Advertisement.objects.filter(creator=user,
                                        status=Advertisement.AdvertisementStatusChoices.OPEN).count() >= 10 and attrs.get(
                'status') != Advertisement.AdvertisementStatusChoices.CLOSED:
            raise serializers.ValidationError("У пользователя не может быть больше 10 открытых объявлений.")
        return attrs