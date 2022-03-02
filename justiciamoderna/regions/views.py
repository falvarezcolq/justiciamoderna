"""Region views"""
from django_filters.rest_framework import DjangoFilterBackend
# Filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import mixins,viewsets,status

from django_countries.templatetags.countries import get_countries
from justiciamoderna.regions.models import Region
from .serializers import RegionModelSerializer

class CountryView(APIView):

    def get(self,request,*args,**kwargs):
        data={
            "countries":get_countries()
        }
        return Response(data)



class RegionViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Regionviewset """


    queryset =  Region.objects.all()
    serializer_class = RegionModelSerializer

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    ordering = ('name',)
    ordering_fields = ('name',)
    search_fields = ('name')
    filterset_fields = ['country']
