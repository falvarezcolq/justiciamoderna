""" Lawyer ViewSet """

# Django
# From REST Framework
from rest_framework import mixins,viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

# models
from justiciamoderna.users.models import Lawyer
# Serializers
from justiciamoderna.users.api.serializers.lawyer import LawyerModelSerializer
from justiciamoderna.users.api.serializers.areas import AreaModelSerializer
class LawyerViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerModelSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def areas(self,request,*args,**kwargs):
        lawyer = self.get_object()
        q_areas = lawyer.areas.all()
        serializer = AreaModelSerializer(q_areas,many=True)
        return Response(serializer.data)


