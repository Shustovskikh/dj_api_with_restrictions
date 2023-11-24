from django_filters import rest_framework as filters
from advertisements.models import Advertisement

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    status = filters.ChoiceFilter(choices=Advertisement.AdvertisementStatusChoices.choices)
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']