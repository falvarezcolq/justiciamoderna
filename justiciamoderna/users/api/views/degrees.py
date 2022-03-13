"""Degrees View"""
# Django
# Rest Framework
from rest_framework import mixins,viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Models
from justiciamoderna.users.models import Degree
# Serializer
from ..serializers.degrees import DegreeModelSerializer

class DegreeViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Degree.objects.all()
    serializer_class = DegreeModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get_queryset(self):
        user = self.request.user
        return Degree.objects.filter(user=user)
