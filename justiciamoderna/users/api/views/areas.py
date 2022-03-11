"""Degrees View"""
# Django
# Rest Framework
from rest_framework import mixins,viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
# Models
from justiciamoderna.users.models import Area
# Serializer
from ..serializers.areas import AreaModelSerializer

class AreaViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Area.objects.all()
    serializer_class = AreaModelSerializer
    permission_classes = [AllowAny]
