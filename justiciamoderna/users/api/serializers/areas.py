"""Area Serializer"""

# Django
from django.utils.translation import ugettext_lazy as _
# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import ValidationError
# models
from justiciamoderna.users.models import Area,Lawyer




class AreaModelSerializer(serializers.ModelSerializer):
    """Area model serializer"""
    class Meta:
        model = Area
        fields = '__all__'

class AddAreaToLawyerSerializer(serializers.Serializer):
    """ADD area to lawyer"""
    area_id = serializers.IntegerField()

    def validate_area_id(self,data):
        try:
            self.context['area'] = Area.objects.get(pk=data)
        except Area.DoesNotExist:
            raise ValidationError(_("Area id does not exists"))

    def validate(self, attrs):
        # self.context['lawyer'] = self.context['request'].user.lawyer
        try:
            self.context['lawyer'] = self.context['request'].user.lawyer
        except Lawyer.DoesNotExist:
            # justiciamoderna.users.models.users.User.lawyer.RelatedObjectDoesNotExist:
            raise ValidationError(_("User have not lawyer account"))

        if self.context['area'] in self.context['lawyer'].areas.all():
            raise ValidationError(_("User already have this area added"))

        return attrs

    def create(self,data):
        area_obj = self.context['area']
        lawyer_obj =self.context['lawyer']
        lawyer_obj.areas.add(area_obj)
        return area_obj

