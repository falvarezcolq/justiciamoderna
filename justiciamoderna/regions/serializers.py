"""Regions serializers."""
from rest_framework.serializers import ModelSerializer
from .models import Region

class RegionModelSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields=[
            "id",
            "name",
            "country",
            ]
