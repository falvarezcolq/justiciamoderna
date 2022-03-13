"""Degrees View"""
# Django
from django.utils.translation import ugettext_lazy as _
# Rest Framework
from rest_framework import mixins,viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import action
from rest_framework.validators import ValidationError

# Models
from justiciamoderna.users.models import Area,Lawyer
# Serializer
from ..serializers.areas import AreaModelSerializer,AddAreaToLawyerSerializer

class LawyerAreaViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Area.objects.all()
    serializer_class = AreaModelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = AddAreaToLawyerSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        object = serializer.save()
        headers = self.get_success_headers(AreaModelSerializer(object).data)
        return Response(AreaModelSerializer(object).data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            lawyer = request.user.lawyer
        except Lawyer.DoesNotExist:
            # raise ValidationError(_("User have not lawyer account"))
            return Response(status=status.HTTP_404_NOT_FOUND)

        if instance not in lawyer.areas.all():
            return Response(status=status.HTTP_404_NOT_FOUND)

        lawyer.areas.remove(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_queryset(self):
        """Return lawyer's areas."""

        try:
            lawyer = self.request.user.lawyer
        except Lawyer.DoesNotExist:
            # raise ValidationError(_("User have not lawyer account"))
            return Response(status=status.HTTP_404_NOT_FOUND)

        return lawyer.areas.all()


