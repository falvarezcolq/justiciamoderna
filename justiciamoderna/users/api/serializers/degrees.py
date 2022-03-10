"""Degree Serializers"""

# Model
import pdb

from justiciamoderna.users.models import Degree
# Rest Framework
from rest_framework import serializers

class DegreeModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    img_l = serializers.ImageField(required=True)
    class Meta:
        model = Degree
        fields = '__all__'


    def create(self, data):
        instance = Degree.objects.create(**data)
        return instance
